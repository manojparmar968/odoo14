from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'student'
    _inherit = ['mail.thread']
    _description = 'student'

    name = fields.Char("Name")
    Roll_no = fields.Integer("Roll No")
    mobile_no = fields.Integer("Mobile Number")
    mobile = fields.Char(string='Mobile Number', size=10)
    teacher_subject_line_ids = fields.One2many(comodel_name="student.teacher",inverse_name="teacher_id")
    Stage = fields.Selection(string='Stage',
        selection=[
            ('fees_not_paid', 'fees not paid'),
            ('fees_paid', 'Fees Paid')
        ], default='fees_not_paid',
    )
    student_class = fields.Selection(string='class',
        selection=[
            ('1', '1'), 
            ('2', '2'),
            ('3', '3')
        ],
    )
    Section = fields.Selection(string='Section',
        selection=[
            ('a', 'A'), 
            ('b', 'B'),
            ('c', 'C')
        ],
    )
    Is_active = fields.Boolean("Active", tracking=True)
    fees_Paid_month = fields.Selection(string='Fees Paid Month',
        selection=[
            ('jan', 'January'), 
            ('feb', 'Feburary'),
            ('march', 'March'),
            ('april', 'April')
        ],
    )
    fees_paid_amount = fields.Float("Fees Paid Amount")
    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        default=lambda self: self.env.user.company_id.currency_id.id
    )
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company
    )
   
    @api.constrains('mobile','mobile_no')
    def _check_mobile_length(self):
        for i in self:
            if i.mobile and len(i.mobile) != 10:
                raise ValidationError('Mobile number must have 10 digits.')
        for i in self:
            if i.mobile_no and len(str(i.mobile_no)) != 10:
                raise ValidationError('Mobile number must have 10 digits.')

    def action_confirm(self):
        if self.Stage == 'fees_not_paid':
            self.Stage = 'fees_paid'
    
    @api.onchange('fees_Paid_month')
    def onchange_fees_Paid_month(self):
        if self.fees_Paid_month == 'jan' and self.Stage == 'fees_paid':
            self.Stage = 'fees_not_paid'
        if self.fees_Paid_month == 'feb' and self.Stage == 'fees_paid':
            self.Stage = 'fees_not_paid'
        if self.fees_Paid_month == 'march' and self.Stage == 'fees_paid':
            self.Stage = 'fees_not_paid'
        if self.fees_Paid_month == 'april' and self.Stage == 'fees_paid':
            self.Stage = 'fees_not_paid'

    _sql_constraints = [
        ('unique_mobile', 'unique (mobile)', 'Mobile number must be unique.'),
       
    ]
