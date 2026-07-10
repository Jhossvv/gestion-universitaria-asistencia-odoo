from odoo import models, fields

class UniversidadCarrera(models.Model):
    _name = 'estudiante.carrera'
    _description = 'Carrera Universitaria'

    name = fields.Char(string='Nombre de la Carrera', required=True)
    codigo = fields.Char(string='Código de Carrera')

    materia_ids = fields.One2many('estudiante.materia', 'carrera_id', string='Plan de Estudios')