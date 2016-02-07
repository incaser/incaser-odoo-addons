# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, api
from openerp import exceptions
from openerp.tools.translate import _
# from openerp.addons.portal.wizard import portal_wizard

# welcome email sent to portal users
WELCOME_EMAIL_SUBJECT = _("Your account at %(company)s")
WELCOME_EMAIL_BODY = _("""Dear %(name)s,

You have been given access to %(company)s's %(portal)s.

Your login account data is:
  Username: %(login)s
  Portal: %(portal_url)s
  Database: %(db)s

You can set or change your password via the following url:
   %(signup_url)s

%(welcome_message)s

""")


class WizardUser(models.TransientModel):
    """
        A model to configure users in the portal wizard.
    """
    _inherit = 'portal.wizard.user'

    @api.model
    def _send_email(self, wizard_user):
        """ send notification email to a new portal user
            @param wizard_user: browse record of model portal.wizard.user
            @return: the id of the created mail.mail record
        """
        res_partner = self.env['res.partner']
        this_context = self._context
        this_user = self.env['res.users'].sudo().browse(self._uid)
        if not this_user.email:
            raise exceptions.Warning(_('Email Required'),
                _('You must have an email address in your User Preferences to send emails.'))

        # determine subject and body in the portal user's language
        user = self.sudo()._retrieve_user(wizard_user)
        context = dict(this_context or {}, lang=user.lang)
        ctx_portal_url = dict(context, signup_force_type_in_url='')
        portal_url = res_partner.with_context(ctx_portal_url)._get_signup_url_for_action(ids=[user.partner_id.id])[user.partner_id.id]
        res_partner.with_context(context).signup_prepare([user.partner_id.id])

        data = {
            'company': this_user.company_id.name,
            'portal': wizard_user.wizard_id.portal_id.name,
            'welcome_message': wizard_user.wizard_id.welcome_message or "",
            'db': self._cr.dbname,
            'name': user.name,
            'login': user.login,
            'signup_url': user.signup_url,
            'portal_url': portal_url,
        }
        mail_mail = self.env['mail.mail']
        mail_values = {
            'email_from': this_user.email,
            'email_to': user.email,
            'subject': _(WELCOME_EMAIL_SUBJECT) % data,
            'body_html': '<pre>%s</pre>' % (_(WELCOME_EMAIL_BODY) % data),
            'state': 'outgoing',
            'type': 'email',
        }
        mail_id = mail_mail.with_context(this_context).create(mail_values)
        return mail_mail.with_context(this_context).send([mail_id])
