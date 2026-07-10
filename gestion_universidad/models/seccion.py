from odoo import models, fields

class UniversidadSeccion(models.Model):
    _name = 'estudiante.seccion'
    _description = 'Sección Universitaria'

    name = fields.Char(string='Nombre de la Sección (Ej. A, B)', required=True)
    turno = fields.Selection([
        ('manana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche')
    ], string='Turno', default='manana')

    # --- NUEVOS CAMPOS ---
    carrera_id = fields.Many2one('estudiante.carrera', string='Carrera', required=True)
    semestre = fields.Selection([
        ('1', '1er Semestre'),
        ('2', '2do Semestre'),
        ('3', '3er Semestre'),
        ('4', '4to Semestre'),
        ('5', '5to Semestre'),
        ('6', '6to Semestre'),
        ('7', '7mo Semestre'),
        ('8', '8vo Semestre'),
    ], string='Semestre', required=True)