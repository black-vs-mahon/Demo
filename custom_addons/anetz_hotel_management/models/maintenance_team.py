# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceTeam(models.Model):
    _name = "maintenance.team"
    _description = "Maintenance Team"

    name = fields.Char(string='Maintenance Team', help='Name of the maintenance team')
    user_id = fields.Many2one('res.users', string='Team Leader', help="Leader of Team",
        domain=lambda self: [('groups_id', 'in', self.env.ref('anetz_hotel_management.maintenance_team_group_leader').id)])
    member_ids = fields.Many2many('res.users', string='Members', help="Members of the Team",
        domain=lambda self: [('groups_id', 'in', self.env.ref('anetz_hotel_management.maintenance_team_group_user').id)])
