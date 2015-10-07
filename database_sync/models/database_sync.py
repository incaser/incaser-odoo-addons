# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class DatabaseSyncServer(models.Model):
    """Remote servers information"""

    _name = "database.sync.server"
    _description = "Remote Server"

    name = fields.Char('Server name', required=True)
    server_url = fields.Char('Server URL', required=True)
    server_port = fields.Integer('Server Port', required=True, default=8069)
    server_db = fields.Char('Server Database', required=True)
    login = fields.Char('User Name', required=True)
    password = fields.Char('Password', required=True)
    model_ids = fields.One2many(
        'database.sync.models', 'server_id', string='Models',
        ondelete='restrict')


class DatabaseSyncModels(models.Model):
    """Models to sync"""

    _name = "database.sync.server"
    _description = "Models to sync"

    name = fields.Char('Server name', required=True)
    server_url = fields.Char('Server URL', required=True)
    server_port = fields.Integer('Server Port', required=True, default=8069)
    server_db = fields.Char('Server Database', required=True)
    login = fields.Char('User Name', required=True)
    password = fields.Char('Password', required=True)
    model_ids = fields.One2many(
        'models.sync.models', 'server_id', string='Models',
        ondelete='restrict')

