from odoo import api, fields, models

class Student(models.Model):
    # Model name and description
    _name = 'school.student'
    _description = 'Student'

    # Fields
    name = fields.Char(string='Nombre', required=True)
    birth_date = fields.Date(string='Año de Nacimiento')
    age = fields.Integer(compute='_compute_age', string='Edad')
    final_exam_grade = fields.Float(string='Nota de Examen Final')
    subject_ids = fields.Many2many('school.subject', string='Materias')

    # Proposed Fields
    grade_ids = fields.One2many('school.grade', 'student_id', string='Nota de Materias')
    average_grade = fields.Float(string='Promedio de Materias', compute='_compute_average_grade')

    # Computed Fields
    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                student.age = (fields.Date.today() - student.birth_date).days // 365

    @api.depends('final_exam_grade', 'grade_ids.grade')
    def _compute_average_grade(self):
        for student in self:
            total_grade = student.final_exam_grade
            subject_count = len(student.grade_ids)
            if subject_count > 0:
                total_grade += sum(subject.grade for subject in student.grade_ids)
                student.average_grade = total_grade / (subject_count + 1)
            else:
                student.average_grade = student.final_exam_grade
