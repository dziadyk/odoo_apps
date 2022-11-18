from odoo import api, exceptions, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def constrains_email(self):
        for rec in self:
            exist_email = self.env['res.partner'].search_count(
                [('id', '!=', rec.id),
                 ('email', '=', rec.email)])
            if exist_email:
                error = 'Email has already been taken'
                raise exceptions.ValidationError(_(error))
