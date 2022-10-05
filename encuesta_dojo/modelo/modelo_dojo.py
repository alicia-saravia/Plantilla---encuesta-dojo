from encuesta_dojo.configuracion.mysqlconnection import connectToMySQL
from flask import flash

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['comentario']
        self.crado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    #Validación de informacion
    @staticmethod
    def validar_dojo(dojo):
        is_valid = True # asumimos que esto es true
        if len(dojo['nombre']) < 4:
            flash("Nombre debe al menos 3 caracteres.")
            is_valid = False        
        return is_valid

    @classmethod
    def crear_dojo(cls, data):
        query = "INSERT INTO dojos (nombre) VALUES (%(nombre)s);"
        resultado = connectToMySQL('Dojos').query_db(query, data)
        return resultado


