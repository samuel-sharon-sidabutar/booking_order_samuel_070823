import datetime, time
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ReportWorkOrder(models.AbstractModel):
    _name = 'report.booking_order_samuel_070823.report_work_order'

    @api.model
    def render_html(self, docids, data=None):
        print(docids)
        work_order_id = None
        for id in docids:
            work_order_id = id
        
        work_order_record = self.env['booking_order_samuel_070823.work_order'].search([('id', '=', work_order_id)])

        print("Sebelum docargs")
        wo_data = {
            # 'wo_number' : data.get['wo_number'],
            # 'team_name' : data.get['team_name'],
            # 'bo_ref' : data.get['booking_order_num'],
            # 'customer': data.get['customer'],
            # 'date_start': data.get['date_start'],
            # 'date_end': data.get['date_end'],
            # 'notes': data.get['notes'],
            'wo_number' : work_order_record.wo_number,
            'team_name' : work_order_record.team.name,
            'bo_ref' : work_order_record.booking_order_reference.name,
            'customer': work_order_record.booking_order_reference.partner_id.name,
            'date_start': work_order_record.date_start,
            'date_end': work_order_record.date_end,
            'notes': work_order_record.notes,
        }
        docargs = {
            'wo_data': wo_data,
            'wo': work_order_record
        }
        print("setelah docargs")
        print(docargs)
        return self.env['report'].render('booking_order_samuel_070823.report_work_order', values=docargs)