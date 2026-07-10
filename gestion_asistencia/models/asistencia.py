from odoo import models, fields, api

class RegistroAsistencia(models.Model):
    _name = 'asistencia.registro'
    _description = 'Registro Diario de Asistencia'
    _rec_name = 'materia_id'

    name = fields.Char(string='Descripción', default='Nueva Asistencia', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    
    materia_id = fields.Many2one('estudiante.materia', string='Materia', required=True)
    seccion_univ_id = fields.Many2one('estudiante.seccion', string='Sección', required=True)
    linea_ids = fields.One2many('asistencia.linea', 'asistencia_id', string='Líneas de Asistencia')

    def accion_cargar_estudiantes(self):
        self.ensure_one()
        self.linea_ids = [(5, 0, 0)]
        
        estudiantes_inscritos = self.env['estudiante.estudiante'].search([
            ('materia_ids', 'in', self.materia_id.id),
            ('seccion_univ_id', '=', self.seccion_univ_id.id)  
        ])
        
        nuevas_filas = []
        for estudiante in estudiantes_inscritos:
            nuevas_filas.append((0, 0, {
                'estudiante_id': estudiante.id,
                'estado': 'presente'
            }))
        
        self.linea_ids = nuevas_filas
        return True

class AsistenciaLinea(models.Model):
    _name = 'asistencia.linea'
    _description = 'Línea de Asistencia'

    asistencia_id = fields.Many2one('asistencia.registro', ondelete='cascade')
    estudiante_id = fields.Many2one('estudiante.estudiante', string='Estudiante', required=True)
    
    estado = fields.Selection([
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),
        ('retraso', 'Retraso')
    ], string='Estado', default='presente', required=True)