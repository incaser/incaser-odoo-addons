# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, api
from openerp.addons.portal.wizard.portal_wizard import extract_email


class WizardUser(models.TransientModel):
    _inherit = 'portal.wizard.user'

    @api.model
    def _create_user(self, wizard_user):
        """ create a new user for wizard_user.partner_id
            @param wizard_user: browse record of model portal.wizard.user
            @return: browse record of model res.users
        """
        res_users = self.env['res.users']
        ctx = self.env.context.copy()
        # to prevent shortcut creation
        ctx.update({
            'noshortcut': True,
            'no_reset_password': True
        })
        values = {
            'email': extract_email(wizard_user.email),
            'login': wizard_user.partner_id.vat,
            'partner_id': wizard_user.partner_id.id,
            'groups_id': [(6, 0, [])],
        }
        return res_users.with_context(ctx).create(values)
