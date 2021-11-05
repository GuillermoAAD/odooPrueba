from odoo import models, fields

#creando modelo(tabla BD) a partir de una clase
class Libros(models.Model):
   _name='libros' #nombre de la tabla

   name = fields.Char(string="Nombre del libro", required=True)
   editorial = fields.Char(string="Editorial",required=True)
   isbn = fields.Char(string="ISBN",required=True)
   autor_id = fields.Many2one(comodel_name="autores", string="Autor", required=True)
   image = fields.Binary(string="Image")