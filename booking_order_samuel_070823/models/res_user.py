from odoo import _, api, fields, models


class ResUser(models.Model):
    _inherit = 'res.users'

    sale_orders = fields.Many2many('sale.order', string='Sale order')
    work_orders = fields.Many2many('booking_order_samuel_070823.work_order', string='Work order')

