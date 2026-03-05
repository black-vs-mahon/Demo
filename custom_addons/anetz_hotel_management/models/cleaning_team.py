# -*- coding: utf-8 -*-
from odoo import fields, models


class CleaningTeam(models.Model):
    _name = "cleaning.team"
    _description = "Cleaning Team"

    name = fields.Char(string="Team Name", help="Name of the Team")
    team_head_id = fields.Many2one('res.users', string="Team Head", help="Choose the Team Head",
        domain=lambda self: [('groups_id', 'in', self.env.ref('anetz_hotel_management.cleaning_team_group_head').id)])
    member_ids = fields.Many2many('res.users', string="Member", help="Team Members",
        domain=lambda self: [('groups_id', 'in', self.env.ref('anetz_hotel_management.cleaning_team_group_user').id)])
