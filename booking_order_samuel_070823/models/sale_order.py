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

    @api.model
    def create(self, vals):
        obj = super(SaleOrder, self).create(vals)
        obj.write({'is_booking_order': True})
        return obj

    @api.onchange('team')
    def set_team_data(self):
        team = self.env['booking_order_samuel_070823.service_team'].search([('id','=',self.team.id)])
        self.leader = team.leader
        self.members = team.members