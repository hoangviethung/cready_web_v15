# -*- coding: utf-8 -*-
{
    'name': 'Cready Theme Backend',
    'summary': 'Cready Theme Backend',
    'version': '1.0',
    'author': 'Hoàng Việt Hùng',
    'category': 'Administration',
    'maintainer': 'Hoàng Việt Hùng',
    'company': 'Cready',
    'support': '',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        # Odoo
        'web'
    ],
    'installable': True,
    'data': [
    ],
    'qweb': [],
    'assets':{
        'web._assets_primary_variables': [
            '/cready_web/static/src/scss/primary_variables.scss',
            '/cready_web/static/src/webclient/navbar/navbar.variables.scss',
        ],
        'web._assets_backend_helpers': [
            '/cready_web/static/src/scss/boostrap_overridden.scss',
        ],
    },
    'application': True,
}