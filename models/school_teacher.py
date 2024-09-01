from odoo import api, fields, models

class Teacher(models.Model):
    # Model name and description
    _name = 'school.teacher'
    _description = 'Teacher'

    # Fields
    user_id = fields.Many2one('res.users', string='User', required=True)
    name = fields.Char(string='Nombre', required=True)
    profile = fields.Text(string='Perfil')
    subject_ids = fields.One2many('school.subject', 'teacher_id', string='Materias')


