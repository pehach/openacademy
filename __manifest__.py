# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """Manage trainings for MSF""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        #'views/views.xml',
		#'views/templates.xml',
		'views/openacademy.xml',
		#'views/views.xml',
		'views/partner.xml',
		'views/session_board.xml',
		'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	
    'installable': True,
    'application': True,
    'auto_install': False,
}