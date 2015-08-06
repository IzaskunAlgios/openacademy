# b-*- encoding: utf-8 -*-

from openerp import models, fields

class Users(models.Model):
    _inherit = 'res.users'
    
    instructor = fields.Boolean(string="Is an instructor?")
    course_ids = fields.One2many(comodel_name='openacademy.course', inverse_name='responsible_id', string='Courses')
