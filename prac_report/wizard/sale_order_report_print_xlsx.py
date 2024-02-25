from odoo import api, fields, models, _
import base64
import io

class SaleOrderReportPrintXlsx(models.AbstractModel):
    _name = 'report.prac_report.sale_order_report_print_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'report prac_report sale_order_report_print_xlsx'

    def generate_xlsx_report(self, workbook, data, partners):
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True})
        format_2 = workbook.add_format({'align': 'right'})
        format_3 = workbook.add_format({'bold': True,'align': 'center', 'bg_color': 'yellow'})
        
        format_1.set_border(3)
        format_2.set_border(3)

        for obj in partners:
            report_name = 'sale Detail'
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31]) # add_worksheet will add new worksheet in excel.
            # sheet.write(0, 0, obj.name, bold) # in sheet 0,0 we will adding static values
            sheet.set_column('D:D',12)
            sheet.set_column('E:E',30)
            row = 2
            col  = 3
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'Sale Details', format_3)
            row += 1