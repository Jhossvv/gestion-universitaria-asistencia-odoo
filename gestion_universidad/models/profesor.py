from odoo import models, fields, api
from odoo.exceptions import ValidationError
class UniversidadProfesor(models.Model):
    _name = 'estudiante.profesor'
    _description = 'Profesor Universitario'
    
    name = fields.Char(string='Nombre y Apellido', required=True)
    cedula = fields.Char(string='Cédula', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    
    materia_ids = fields.Many2many('estudiante.materia','profesor_id', string='Materias que dicta')
    carrera_ids = fields.Many2many('estudiante.carrera', string='Carreras Asignadas')
    seccion_ids = fields.Many2many('estudiante.seccion', string='Secciones Asignadas')
    
    @api.constrains('cedula', 'telefono')
    def _check_cedula_telefono(self):
        for record in self:
            if not record.cedula or not record.telefono:
                raise ValidationError("La cédula y el teléfono son obligatorios.")
    
    def cedula_telefono_unicos(self):
        for record in self:
            existing_profesor = self.env['universidad.profesor'].search([
                ('id', '!=', record.id),
                '|',
                ('cedula', '=', record.cedula),
                ('telefono', '=', record.telefono)
            ], limit=1)
            if existing_profesor:
                raise ValidationError("La cédula o el teléfono ya están registrados para otro profesor.")   