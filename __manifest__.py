# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': 
        """
        Desarrollo de un módulo de gestión de una escuela 
        Reto de Odoo 16.0
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Andre Argandoña",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/school_security.xml',
        'views/school_student_views.xml',
        'views/school_teacher_views.xml',
        'views/school_subject_views.xml',
        'views/menu_item_views.xml',
        'security/ir.model.access.csv',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
