{
    'name': 'Gestión Universitaria',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Sistema integral para el manejo de estudiantes, profesores, carreras y materias.',
    'description': """
        Módulo de Gestión Universitaria
        ===============================
        Este módulo permite administrar la estructura académica de una universidad.
        Incluye características como:
        - Registro de Estudiantes y Profesores.
        - Estructuración de Carreras y Secciones por turnos.
        - Asignación de Materias dinámicas mediante filtros.
        - Arquitectura relacional optimizada en PostgreSQL.
    """,
    'author': 'Jhosert Sneider Sánchez Varón',
    'website': 'https://github.com/Jhossvv',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estudiantes_views.xml',
        #'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}