# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class KsDashboardmtnBoardItemAction(models.TransientModel):
    _name = 'ks_mtn_dashboard.item_action'
    _description = 'Dashboard mtn Item Actions'

    name = fields.Char()
    ks_dashboard_item_ids = fields.Many2many("ks_dashboard_mtn.item", string="عناصر لوحة المعلومات")
    ks_action = fields.Selection([('move', 'Move'),
                                  ('duplicate', 'Duplicate'),
                                  ], string="Action")
    ks_dashboard_mtn_id = fields.Many2one("ks_dashboard_mtn.board", string="حدد لوحة المعلومات")
    ks_dashboard_mtn_ids = fields.Many2many("ks_dashboard_mtn.board", string="حدد لوحات المعلومات")

    # Move or Copy item to another dashboard action

    def action_item_move_copy_action(self):
        if self.ks_action == 'move':
            for item in self.ks_dashboard_item_ids:
                item.ks_dashboard_mtn_board_id = self.ks_dashboard_mtn_id
        elif self.ks_action == 'duplicate':
            # Using sudo here to allow creating same item without any security error
            for dashboard_id in self.ks_dashboard_mtn_ids:
                for item in self.ks_dashboard_item_ids:
                    item.sudo().copy({'ks_dashboard_mtn_board_id': dashboard_id.id})
