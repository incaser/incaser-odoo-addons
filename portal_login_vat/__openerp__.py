# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Portal Login Vat",
    "summary": "Do login with vat partner",
    "version": "8.0.1.0.0",
    "category": "Tools",
    "website": "https://odoo-community.org/",
    'author': 'Incaser Informatica S.L., '
              'Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "portal",
        "auth_signup",
    ],
    "data": [
        "views/auth_view.xml",
    ],
}
