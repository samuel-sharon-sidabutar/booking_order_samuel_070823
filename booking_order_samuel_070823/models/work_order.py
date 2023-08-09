from odoo import _, api, fields, models
from odoo.osv import osv
from datetime import datetime


class WorkOrder(models.Model):
    _name = 'booking_order_samuel_070823.work_order'
    _description = 'Work Order'

    wo_number = fields.Char(string='WO Number', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('increment_wo_number'))
    booking_order_reference = fields.Many2one('sale.order', string='Booking Order Reference', readonly=True)
    team = fields.Many2one('booking_order_samuel_070823.service_team', string='Service Team', required=True)
    leader = fields.Many2one('res.users', string='Team Leader', required=True)
    members = fields.Many2many('res.users', string='Team Members')
    planned_start = fields.Datetime(string='Planned Start', required=True)
    planned_end = fields.Datetime(string='Planned End', required=True)
    date_start = fields.Datetime(string='Date Start', readonly=True)
    date_end = fields.Datetime(string='Date End', readonly=True)
    state = fields.Selection([('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], string='Status', default='pending')
    notes = fields.Text(string='Notes')

    @api.multi
    def action_start_work(self):
        self.state = 'in_progress'
        self.date_start = datetime.now()
    
    @api.multi
    def action_end_work(self):
        self.state ='done'
        self.date_end = datetime.now()

    @api.multi
    def action_reset(self):
        self.state ='pending'
    
    @api.multi
    def action_cancel(self):
        self.state ='cancelled'
        # CREATE WIZZARD ASKING FOR CANCELLATION NOTE