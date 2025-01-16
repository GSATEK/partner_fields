from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_external_reference = fields.Char(
        string="Referencia Externa del Proveedor",
        related='partner_id.x_external_reference',
        store=True,
    )
