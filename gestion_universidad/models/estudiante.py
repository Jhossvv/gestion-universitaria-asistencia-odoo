from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Estudiante(models.Model):
    _name = 'estudiante.estudiante'  
    _description = 'Información del Estudiante'
    _rec_name = 'nombre'  
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    cedula = fields.Char(string='Cédula', required=True)
    semestre = fields.Selection([
        ('1', 'Primer Semestre'),
        ('2', 'Segundo Semestre'),
        ('3', 'Tercer Semestre'),
        ('4', 'Cuarto Semestre'),
        ('5', 'Quinto Semestre'),
        ('6', 'Sexto Semestre'),
        ('7', 'Séptimo Semestre'),
        ('8', 'Octavo Semestre'),
    ], string='Semestre', required=True)
    
    carrera_id = fields.Many2one('estudiante.carrera', string='Carrera', required=True)
    
    seccion_univ_id = fields.Many2one('estudiante.seccion', string='Sección', required=True)
    
    materia_ids = fields.Many2many(
        comodel_name='estudiante.materia',
        relation='estudiante_materia_rel', 
        column1='estudiante_id', 
        column2='materia_id',        
        string='Materias Inscritas'
    )
    
    @api.constrains('cedula')
    def _check_cedula_unica(self):
        for record in self:
            if record.cedula:
                registros_existentes = self.search_count([('cedula', '=', record.cedula)])
                if registros_existentes > 1:
                    raise ValidationError(f"¡Atención! Ya existe un estudiante registrado con la cédula {record.cedula}.")
