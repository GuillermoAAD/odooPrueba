from odoo import models, fields

#creando modelo(tabla BD) a partir de una clase
class Autor(models.Model):
   _name='autores' #nombre de la tabla

   name = fields.Char(string="Nombre del autor", required=True)


