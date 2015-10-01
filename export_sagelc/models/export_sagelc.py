# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, api

class base_external_dbsource(models.Model):
    _inherit = "base.external.dbsource"

    @api.multi
    def execute_void(self, sqlquery, sqlparams=None, metadata=False):
        for obj in self:
            conn = obj.conn_open(obj.id)
            cur = conn.cursor()
            res = cur.execute(sqlquery, sqlparams)
            conn.commit()
            conn.close()
        return res
