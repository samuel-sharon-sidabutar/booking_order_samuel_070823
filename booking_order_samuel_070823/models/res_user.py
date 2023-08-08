from odoo import _, api, fields, models


class ResUser(models.Model):
    _inherit = 'res.users'

    sale_orders = fields.Many2many('sale.order', string='Sale order')

