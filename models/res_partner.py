from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_external_reference = fields.Char(string='Referencia Externa')
