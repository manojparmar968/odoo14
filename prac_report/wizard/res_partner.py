from odoo import api, fields, models, _


class ResPartnerWizard(models.TransientModel):
    _name = 'res.partner.report.wizard'
    _description = "res partner report wizard"

    # _id = fields.Many2one('', string='')
    # display_invoice_alert = fields.Boolean()
    gender = fields.Selection(string='Gender',
        selection=[
            ('male', 'Male'),
            ('female', 'FeMale'),
            ('other', 'Other')
        ]
    )
    age = fields.Integer("Age")

# class ResPartner(models.TransientModel):
#     _inherit = 'res.partner'