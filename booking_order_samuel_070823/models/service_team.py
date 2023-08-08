from odoo import _, api, fields, models


class ServiceTeam(models.Model):
    _name = 'booking_order_samuel_070823.service_team'
    _description = 'Service Team'

    name = fields.Char(string='Team Name', required=True)
    leader = fields.Many2one('res.users', string='Team Leader', required=True)
    members = fields.Many2many('res.users', string='Team Members')
