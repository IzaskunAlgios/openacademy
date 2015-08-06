# b-*- encoding: utf-8 -*-
#'views/res_users_ext.xml',
{
    'name': 'Open Academy',
    'version': '1.0',
    'author': 'Algios',
    'category': 'Education',
    'description': 'Module for the management of an Open Academy.',
    'depends': ['base'],
    'data': ['views/openacademy_session.xml',
		'views/openacademy_course.xml',
        'views/openacademy_wizard.xml',
		'views/openacademy_menu.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'workflows/session_workflow.xml',
             ],
    'demo': [],
    'installable': True,
     'test': [
    ],

}
