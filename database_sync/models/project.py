# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    external_project_id = fields.Integer(
        string='External Project ID')


class ProjectTask(models.Model):
    _inherit = 'project.task'

    external_task_id = fields.Integer(
        string='External Task ID')

