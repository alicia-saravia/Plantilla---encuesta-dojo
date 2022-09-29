from encuesta_dojo import app
from flask import render_template, request, redirect,session

app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta



@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return render_template('index.html')  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/process',methods=['POST'])
def process():
    formulario = request.form
    session['nombre'] = formulario['nombre']
    session['ubicacion'] = formulario['ubicacion']
    session['lenguaje'] = formulario['lenguaje']
    session['conocimiento'] = formulario['gridRadios']
    session['experiencia'] = formulario.get('experiencia')
    session['comentario'] = formulario['comentario']
    print(session)
    return redirect('/result')

@app.route('/result')
def resultado():
    return render_template("redireccion.html", proceso = session)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404