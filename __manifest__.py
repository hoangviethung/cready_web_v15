# -*- coding: utf-8 -*-
{
    'name': 'Cready Theme Backend',
    'summary': 'Cready Theme Backend Odoo 16',
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
            '/cready_web_v16/static/src/scss/primary_variables.scss',
            '/cready_web_v16/static/src/webclient/navbar/navbar.variables.scss',
        ],
        'web._assets_backend_helpers': [
            '/cready_web_v16/static/src/scss/boostrap_overridden.scss',
        ],
    },
    'application': True,
}