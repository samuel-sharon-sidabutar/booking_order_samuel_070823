from odoo import _, api, fields, models
from odoo.osv import osv


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string='Booking Order')
    team = fields.Many2one('booking_order_samuel_070823.service_team', string='Service Team')
    leader = fields.Many2one('res.users', string='Team Leader')
    members = fields.Many2many('res.users', string='Team Members')
    booking_start = fields.Datetime(string='Booking Start')
    booking_end = fields.Datetime(string='Booking End')