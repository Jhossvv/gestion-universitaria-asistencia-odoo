from odoo import models, fields

class Materia(models.Model):
    _name = 'estudiante.materia'
    _description = 'Materia Universitaria'
    _rec_name = 'name' 

    name = fields.Char(string='Nombre de la Materia', required=True)
    codigo = fields.Char(string='Código de la Materia', required=True)
    creditos = fields.Integer(string='Créditos')
    
    carrera_id = fields.Many2one('estudiante.carrera', string='Carrera', required=True)
    profesor_id = fields.Many2one('estudiante.profesor', string='Profesor Titular')