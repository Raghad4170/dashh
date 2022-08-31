from odoo import models, fields, api, _


class KsDashboardmtnTemplate(models.Model):
    _name = 'ks_dashboard_mtn.board_template'
    _description = 'Dashboard mtn Template'

    name = fields.Char()
    ks_gridstack_config = fields.Char()
    ks_item_count = fields.Integer()
    ks_template_type = fields.Selection([('ks_default', 'Predefined'), ('ks_custom', 'Custom')],
                                        string="قالب لوحة المعلومات")
    ks_dashboard_item_ids = fields.One2many('ks_dashboard_mtn.item', 'ks_dashboard_board_template_id',
                                            string="نوع القالب")
    ks_dashboard_board_id = fields.Many2one('ks_dashboard_mtn.board', string="لوحة المعلومات", help="""
        Items Configuration and their position in the dashboard will be copied from the selected dashboard 
        and will be saved as template.
    """)

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if val.get('ks_template_type', False) and val.get('ks_dashboard_board_id', False):
                dashboard_id = self.env['ks_dashboard_mtn.board'].browse(val.get('ks_dashboard_board_id'))
                val['ks_gridstack_config'] = dashboard_id.ks_gridstack_config
                val['ks_item_count'] = len(dashboard_id.ks_dashboard_items_ids)
                val['ks_dashboard_item_ids'] = [(4, x.copy({'ks_dashboard_mtn_board_id': False}).id) for x in
                                                dashboard_id.ks_dashboard_items_ids]
        recs = super(KsDashboardmtnTemplate, self).create(vals_list)
        return recs

    def write(self, val):
        if val.get('ks_dashboard_board_id', False):
            dashboard_id = self.env['ks_dashboard_mtn.board'].browse(val.get('ks_dashboard_board_id'))
            val['ks_gridstack_config'] = dashboard_id.ks_gridstack_config
            val['ks_item_count'] = len(dashboard_id.ks_dashboard_items_ids)
            val['ks_dashboard_item_ids'] = [(6, 0,
                                             [x.copy({'ks_dashboard_mtn_board_id': False}).id for x in
                                              dashboard_id.ks_dashboard_items_ids])]
        recs = super(KsDashboardmtnTemplate, self).write(val)
        return recs
