# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Test theme',
    'summary': 'Test theme',
    'version': '8.0.1.0.0',
    'category': "Theme/Creative",
    'author': 'Incaser Informatica S.L., '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': ['website', 'website_less'],
    'data': [
        'views/assets.xml',
        'views/images_library.xml',
        'views/layout.xml',
    ],
    'installable': True,
}
