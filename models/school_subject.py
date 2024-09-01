from odoo import api, fields, models

class Subject(models.Model):
    # Model name and description
    _name = 'school.subject'
    _description = 'Subject'

    # Fields
    name = fields.Char(string='Nombre', required=True)
    credits = fields.Integer(string='Créditos')
    max_students = fields.Integer(string='Máximo de Estudiantes')
    active = fields.Boolean(string='Activo', default=True)
    student_ids = fields.Many2many('school.student', string='Estudiantes')
    teacher_id = fields.Many2one('school.teacher', string='Profesor')
    grade_ids = fields.One2many('school.grade', 'subject_id', string='Notas de Estudiantes')
