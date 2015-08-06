# b-*- encoding: utf-8 -*-

from openerp import models, fields

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Course Description")

    responsible_id = fields.Many2one(comodel_name='res.users', string="Responsible")

    session_ids = fields.One2many(comodel_name='openacademy.session', inverse_name='course_id', string="Sessions")







