from odoo import api, fields, models, _
import base64
import io

class ResPartnerXlsx(models.AbstractModel):
    _name = 'report.prac_report.report_template_res_partner_report_wizard'
    _description = 'report prac_report report_template_res_partner_report_wizard'

    @api.model
    def _get_report_values(self,docids, data=None):
        print("\n\n\n\n-----------------------------------------------------------------",docids,"\n",data)
        val = self.env['sale.order'].search([])
        return {
            'val': val,
            'name': 'MANOJ PARMAR',
            'email': 'manoj@gmail.com'
        }