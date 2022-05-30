from odoo import models, fields,api

class department_Register(models.Model):
    _inherit = 'res.company'
    _description = 'department registration'


    name = fields.Char(string="Department name")
    department_ids = fields.One2many('grievance.register','department_id')