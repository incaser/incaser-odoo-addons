# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, fields, models


class PortalWizard(models.TransientModel):
    _inherit = 'portal.wizard'

    select_all = fields.Boolean()
    modified = fields.Boolean()

    @api.onchange('select_all')
    def _onchange_select_all(self):
        # The variable modified avoids that all records set false at load view
        if self.modified:
            for user in self.user_ids:
                user.in_portal = self.select_all
        self.modified = True
