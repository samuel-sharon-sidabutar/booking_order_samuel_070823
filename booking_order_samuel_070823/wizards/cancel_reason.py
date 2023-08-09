from odoo import models, fields, api, _

class CancelReason(models.TransientModel):
    _name = 'booking_order_samuel_070823.cancel_reason'
    _description = 'Reason For Cancellation'

    work_order_id = fields.Many2one('booking_order_samuel_070823.work_order', string="Work Order")
    reason  = fields.Text(string='Notes')

    def action_cancel(self):
        wo_ids = self._context.get('active_ids')
        wo_id = None
        
        for rec in wo_ids:
            wo_id = self.env['booking_order_samuel_070823.work_order'].search([('id', '=', rec)])

        wo_id.notes = self.reason
        wo_id.state ='cancelled'

    
