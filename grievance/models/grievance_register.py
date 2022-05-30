# -*- coding: utf-8 -*-

from email.policy import default
from random import randint
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError,ValidationError

class grievance_Register(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'grievance.register'
    _description = 'grievance registration'

    @api.returns('self')
    def _default_stage(self):
        return self.env['grievance.stage'].search([], limit=1)

    name = fields.Char(string="Subject", required=True)
    image = fields.Image()
    description = fields.Text(required=True)
    supporters_ids = fields.Many2many('res.partner', required=True)
    grievance_type_id = fields.Many2one('grievance.type', required=True)
    department_id = fields.Many2one('res.company')
    stage_id = fields.Many2one('grievance.stage', group_expand='_read_group_stage_ids', default=_default_stage)
    reached_stage = fields.Boolean(default=False)
    status = fields.Selection([('toapproved','To Approve'), ('approved','Approved'),('rejected','Rejected')], required=True, default='toapproved')
    assignees_id = fields.Many2one('res.users')
    active = fields.Boolean(default=True)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """ Read group customization in order to display all the stages in the
            kanban view, even if they are empty
        """
        stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

    # methods for button
    def action_approved(self):
        for rec in self:
            if rec.status == 'rejected':
                raise ValidationError("Rejected grievance can't be Approve")
            rec.status = 'approved'

    def action_rejected(self):
        for rec in self:
            if rec.status == 'approved':
                raise ValidationError("approved grievance can't be reject")
            rec.status = 'rejected'   

    def action_asignme(self):
        for record in self:
            record.assignees_id = self.env.user

    @api.model
    def create(self, vals):
        grievance = super(grievance_Register, self).create(vals)
        for rec in grievance:
            partner_ids = []
            if rec.assignees_id:
                partner_ids.append(rec.assignees_id.partner_id.id)
            if rec.supporters_ids:
                    for supporter in rec.supporters_ids:
                        if supporter.id and supporter.email:
                            partner_ids.append(supporter.id)
                    if partner_ids:
                        rec.message_subscribe(partner_ids, None)
        return grievance

class grievance_Stage(models.Model):
    _name = 'grievance.stage'
    _description = 'grievance stage'
    
    name = fields.Char()
    stage_ids = fields.One2many('grievance.register', 'stage_id')
    