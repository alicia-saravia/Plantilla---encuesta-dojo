from encuesta_dojo import app
from flask import render_template, request, redirect,session
from encuesta_dojo.modelo.modelo_dojo import Dojos

app.secret_key = 'keep it secret, keep it safe' # establece una clave secretas

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return render_template('index.html')  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/process',methods=['POST'])
def process():
    if not Dojos.validar_dojo(request.form):
        return redirect('/')
    Dojos.crear_dojo(request.form)
    return redirect('/')

@app.route('/result')
def resultado():
    return render_template("redireccion.html", proceso = session)

@app.route('/encuesta_dojo', methods=['POST'])
def encuesta_dojo():
    # si hay errores:
    # llamamos al método estático en el modelo Burger para validar
    if not Dojos.validar_dojo(request.form):
        # redirigir a la ruta donde se renderiza el formulario de encuesta dojo
        return redirect('/')
    # de lo contrario, no hay errores:
    Dojos.save(request.form)
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404