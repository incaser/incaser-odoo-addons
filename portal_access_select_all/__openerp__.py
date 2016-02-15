# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Portal Access Select All',
    'summary': 'Select all users in portal access management wizard',
    'version': '8.0.1.0.0',
    'category': 'Portal',
    "website": "https://odoo-community.org/",
    'author': 'Incaser Informatica S.L., '
              'Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "portal",
    ],
    'data': [
        'wizards/portal_wizard_view.xml',
     ],
}
