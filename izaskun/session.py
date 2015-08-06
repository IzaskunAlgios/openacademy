# b-*- encoding: utf-8 -*-
from datetime import timedelta
from openerp import models, fields, api

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(string="Session Name", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")
    duration = fields.Integer(string="Duration in days", default=5)
    seats = fields.Integer(string="Number of seats", default=20)

    # link sessions to courses and instructors
    course_id = fields.Many2one('openacademy.course', string="Course", required=True)
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    
    # link sessions to partners for attendee subscription:
    attendee_ids = fields.Many2many('res.partner')

    taken_seats = fields.Float(
        string="Percentage Taken seats", compute='_compute_taken_seats')
    
    # color for the kanban view
    color = fields.Integer()
    
    # state
    state = fields.Selection([
         ('draft', "Draft"),
         ('confirmed', "Confirmed"),
         ('done', "Done"),
    ], default='draft')

    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_confirm(self):
        self.state = 'confirmed'

    @api.one
    def action_done(self):
        self.state = 'done'

    @api.one
    @api.depends('seats', 'attendee_ids') #cuando cambia el nº de asientos o la lista de asistentes
    def _compute_taken_seats(self):
        if not self.seats:
            self.taken_seats = 0.0
        else:
            # calculate the percentage
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
            
    @api.onchange('seats')
    def _onchange_course(self):
        if self.seats <= 0:
            return {
                'warning': {
                'title': "Warning",
                'message': "The number of seats must be above 0.",
                }
            }

    @api.one
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor(self):
        if self.instructor_id in self.attendee_ids:
            raise Warning("Instructor of session '%s' "
                "cannot attend its own session" % self.name)



