from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StudentSubject(models.Model):
    _name = 'student.teacher'
    _inherit = ['mail.thread']
    _description = 'student teacher'

    teacher_id = fields.Many2one(comodel_name="student",string="Teacher",)