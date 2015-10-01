# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp.osv import fields, osv
from openerp.tools.safe_eval import safe_eval


class WebsiteConfig(osv.osv_memory):
    _name = 'website.config.settings'
    _inherit = ['website.config.settings']

    _columns = {
        'disable_website': fields.boolean(string='Disable website')
    }

    def get_default_disable_website(self, cr, uid, fields, context=None):
        icp = self.pool.get('ir.config_parameter')
        return {
            'disable_website': safe_eval(icp.get_param(
                cr, uid, 'website_maintenance.disable_website', 'False'))
        }

    def set_disable_website(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context=context)
        icp = self.pool.get('ir.config_parameter')
        icp.set_param(cr, uid, 'website_maintenance.disable_website',
                      repr(config.disable_website))
