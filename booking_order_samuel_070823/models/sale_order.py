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
    work_order_count = fields.Integer(compute='compute_count')

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

    @api.multi
    def action_confirm(self):
        overlap, overlapping_with = self.check_for_datetime_overlap()
        if overlap:
            raise osv.except_osv("Overlap detected", "Team is not available during this period, already booked on "+overlapping_with+". Please book on another date.")
        obj = super(SaleOrder, self).action_confirm()
        vals = self.get_work_order_vals()
        wo = self.env['booking_order_samuel_070823.work_order'].create(vals)
        return True

    @api.multi
    def action_check(self):
        overlap, overlapping_with = self.check_for_datetime_overlap()
        if overlap:
            raise osv.except_osv("Overlap detected", "Team already has work order during that period on "+ overlapping_with)
        if not overlap:
            raise osv.except_osv("No overlap is detected", "Team is available for booking")

    def get_work_order_vals(self):
        vals = {
            'state': 'pending',
            'team': self.team.id,
            'leader': self.leader.id,
            'members': [(6,0,self.get_member_ids())],
            # SET IN START AND END ACTIONS
            # 'date_start': self.booking_start,
            # 'date_end': self.booking_end,
            'planned_start': self.booking_start,
            'planned_end': self.booking_end,
            'booking_order_reference': self.id,
        }
        return vals

    def get_member_ids(self):
        member_ids = []
        for rec in self.members:
            member_ids.append(rec.id)
        print(member_ids)
        return member_ids
    
    def check_for_datetime_overlap(self):
        overlap = False
        overlapping_with = None
        active_work_orders = self.env['booking_order_samuel_070823.work_order'].search([('state', '!=', 'cancelled')])
        # print(active_work_orders)
        for work_order in active_work_orders:
            if work_order.team != self.team and work_order.leader != self.leader:
                continue
            if work_order.planned_start <= self.booking_end and work_order.planned_end >= self.booking_start:
                overlap = True
                overlapping_with = work_order.booking_order_reference.name
                continue
        return overlap, overlapping_with
    
    def open_work_order_form(self):
        search_output = self.env['booking_order_samuel_070823.work_order'].search([('booking_order_reference', '=', self.id)])
        print(search_output)
        print(len(search_output))
        if len(search_output) == 0:
            raise osv.except_osv("A work order has not been created for this booking order.")
        return{
            'res_model': 'booking_order_samuel_070823.work_order',
            'res_id': search_output.id,
            'type': 'ir.actions.act_window',
            # 'view_type': 'form', 
            'view_mode': 'form', 
            'view_id': self.env.ref('booking_order_samuel_070823.booking_order_samuel_070823_work_order_view_form').id
        }

    def compute_count(self):
        print(self)
        for rec in self:
            print(rec)
            rec.work_order_count = self.env['booking_order_samuel_070823.work_order'].search_count([('booking_order_reference', '=', self.id)])