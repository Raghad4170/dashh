from odoo import models, fields, api, _


class KsDashboardmtnBoardItemAction(models.Model):
    _name = 'ks_dashboard_mtn.child_board'
    _description = 'Dashboard mtn Child Board'

    name = fields.Char()
    ks_dashboard_mtn_id = fields.Many2one("ks_dashboard_mtn.board", string="حدد لوحة المعلومات")
    ks_gridstack_config = fields.Char('تكوينات العنصر')
    # ks_board_active_user_ids = fields.Many2many('res.users')
    ks_active = fields.Boolean("تم الإختيار")
    ks_dashboard_menu_name = fields.Char(string="اسم القائمة", related='ks_dashboard_mtn_id.ks_dashboard_menu_name', store=True)
    board_type = fields.Selection([('default', 'Default'), ('child', 'Child')])
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)

