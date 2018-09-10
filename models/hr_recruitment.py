# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Applicant(models.Model):
    _inherit = "hr.applicant"

    partner_name = fields.Char(track_visibility='always')
    job_id = fields.Many2one(track_visibility='always')
    department_id = fields.Many2one(track_visibility='always')