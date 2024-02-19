from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentSubject(models.Model):
    _name = 'student.subject'
    _inherit = ['mail.thread']
    _description = 'student subject'

    Subject_ids = fields.Many2many(comodel_name="student", string="Subject")