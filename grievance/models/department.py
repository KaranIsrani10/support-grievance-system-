from odoo import models, fields,api

class department_Register(models.Model):
    _name = 'department.register'
    _description = 'department registration'


    name = fields.Char()
    department_ids = fields.One2many('grievance.register','department_id')