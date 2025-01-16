from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    partner_external_reference = fields.Char(
        string="Referencia Externa del Cliente",
        related='partner_id.x_external_reference',
        store=True,
    )
