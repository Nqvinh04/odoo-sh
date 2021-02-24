# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose cccccccccccc
    """,

    'author': "NQ Vinh",
    'website': "http://www.yourcompany.com",
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'wizards/wizard_view.xml',
        'reports/report.xml',
        'reports/session_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
