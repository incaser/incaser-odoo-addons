# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name" : "Timesheet Line Product",
    "version" : "8.0.1.0",
    "author" : "Incaser Informatica S.L.",
    "category": 'Incaser Plugins',
    'complexity': "easy",
    "description": """
Incaser Plugins - Timesheet Line Product
========================================
This modules show in timesheet line the product field

for OpenERP 8.0
v1.0
    """,
    'website': 'http://www.incaser.es',
    'depends': ['base', 'mail', 'hr_timesheet'],
    'init_xml': [],
    'data': ['views/timesheet_line_view.xml'],
    'demo_xml': [],
    'test': [],
    'application': False,
    'installable': True,
}

