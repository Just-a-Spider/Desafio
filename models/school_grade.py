from odoo import api, fields, models

class Grade(models.Model):
    _name = 'school.grade'
    _description = 'Nota de Estudiante por Materia'

    student_id = fields.Many2one('school.student', string='Estudiante', required=True)
    subject_id = fields.Many2one('school.subject', string='Materia', required=True)
    grade = fields.Float(string='Nota')