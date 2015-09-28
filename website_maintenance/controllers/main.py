# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import http
from openerp.addons.website.controllers.main import Website


class WebsiteDisable(Website):

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        res = super(WebsiteDisable, self).index()
        return res
