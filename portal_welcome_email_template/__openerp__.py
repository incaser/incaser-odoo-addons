# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Portal Welcome Email Template",
    "summary": "Use an email template for send portal invitation",
    "version": "8.0.1.0.0",
    "category": "Portal",
    "website": "https://odoo-community.org/",
    'author': 'Incaser Informatica S.L., '
              'Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "portal",
    ],
    "data": [
        "data/email_template_data.xml",
    ],
}
