# from . import 
"""
@api.multi

@api.constrains('phone_number')

def _check_phone_number(self):

    for rec in self:

         if rec.phone_number and len(rec.phone_number) != 10"

             raise ValidationError(_("laplap..."))

     return True

#constraint
@api.constrains('number')
@api.one
def _check_number(self):
    number = self.number
    if number and len(str(abs(number))) > 4:
	raise ValidationError(_('Number of digits must on exceed 4'))

Create a module named as student

Py fields are:
name(Char)
Roll_no(integer)
Mobile No(Integer and restrict it to 10 digits) also raise error if duplicate mobile no
teacher_subject_line_ids(O2M) and fields associated in this are:
	I. Teacher Name(Many2one)
II. Subject (Many2Many)
Stage as fees_paid, fees_not_paid
Class(selection[I,II,III,etc])
Section(Selection[A,B,C])
Is_active(boolean)[keep tracking]
fees_Paid_month(Selection[Jan,Feb,etc])[will be shown to higher level hierarchy user]
fees_paid_amount(float)

Form View 
Fields to be shown are: 
Stage, name,Roll_no, Mobile,Class,Section,is_active,fees_paid_month
Keep a button named fees_paid which will shift the stage from fees_not_paid -> fees_paid also button will be highlighted only for higher level hierarchy user
If the fees_Paid_month changes then the stage change from fees_paid to fees_not_paid

List view
name,Roll_no, Mobile,Class,Section,is_active(user can hide unhide by user),Stage,fees_Paid_month(user can hide unhide by user),fees_paid_amount with currency
At the bottom of the tree view sum of fees_paid_amount to be shown

Search view
Search can be done with name and mobile no both.
Group by Class and Sections

Security: with 2 levels of hierarchy
Where is_active and fees_paid_month can be edited for the higher level user and remains read only for others users

Create a pdf Report as:
Report name Monthly student fees report as heading
Report print date and time below heading left side and in the same line right side printed by ->user_name
Create a table with columns as name,Roll_no, Mobile,Class,Section,is_active,Stage,fees_Paid_month.

"""