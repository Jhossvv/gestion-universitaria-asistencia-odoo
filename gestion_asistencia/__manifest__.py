{
    'name': 'Gestión de Asistencia',
    'version': '1.0',
    'summary': 'Control de asistencia para estudiantes',
    'author': 'Jhosert Sneider Sánchez Varón',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'gestion_universidad'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/asistencia_views.xml',
    ],
    'installable': True,
    'application': True,
}