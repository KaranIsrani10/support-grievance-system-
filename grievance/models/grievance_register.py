# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

# initial db 
class grievance_Register(models.Model):
    _name = 'grievance.register'
    _description = 'grievance registration'

    name = fields.Char(string="Subject")
    image = fields.Image()
    description = fields.Text()
    supporters_ids = fields.Many2many('res.partner')
    grievance_type_id = fields.Many2one('grievance.type')
    department_id = fields.Many2one('department.register')
    state = fields.Selection([('new','New'),('inprogress','In Progress'),('solved','Solved'),('cancel','Cancelled')], default='new')
    assignees_id = fields.Many2one('res.users')
    active = fields.Boolean(default=True, compute="compute_active_grievance", store=True)

    @api.depends('active','state')
    def compute_active_grievance(self):
        for record in self:
            if record.state == 'solved' or record.state == 'cancel':
                record.active = False

    # methods for button
    def action_inprogress(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Cancelled Grievance can't be In-Progress state")
            record.state = 'inprogress'
    
    def action_solved(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Cancelled Grievance can't be solved state")
            record.state = 'solved'

    def action_cancel(self):
        for record in self:
            if record.state == 'solved':
                raise UserError("Solved Grievance can't be Cancelled state")
            record.state = 'cancel'    