from odoo import api, fields, models, _
import base64
import io

class ResPartnerXlsx(models.AbstractModel):
    _name = 'report.prac_report.report_respartner_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    # https://xlsxwriter.readthedocs.io/ ---> documenattion

    def generate_xlsx_report(self, workbook, data, partners):
        # sheet = workbook.add_worksheet('Partner') # it will add all the data into single sheet with file name Partner.
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True})
        format_2 = workbook.add_format({'align': 'right'})
        format_3 = workbook.add_format({'bold': True,'align': 'center', 'bg_color': 'yellow'})
        
        format_1.set_border(3)
        format_2.set_border(3)

        for obj in partners:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31]) # add_worksheet will add new worksheet in excel.
            # sheet.write(0, 0, obj.name, bold) # in sheet 0,0 we will adding static values
            sheet.set_column('D:D',12)
            sheet.set_column('E:E',30)
            row = 2
            col  = 3
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'User Details', format_3)
            row += 1
            if obj.image_1920:
                user_image = io.BytesIO(base64.b64decode(obj.image_1920))
                sheet.insert_image(row, col, "image.png", {'image_data': user_image, 'x_scale': 0.5, 'y_scale': 0.5})
                row += 5
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col + 1, obj.name) # Dynamic row & col
            row += 1
            sheet.write(row, col, 'Email', bold)
            sheet.write(row, col + 1, obj.email)
            row += 1
            sheet.write(row, col, 'Phone', bold)
            sheet.write(row, col + 1, obj.phone)

            row += 2