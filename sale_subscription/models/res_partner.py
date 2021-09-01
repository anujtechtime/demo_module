# -*- coding: utf-8 -*-
# © 2014 - 2017 Sudokeys (Nicolas Potier <nicolas.potier@sudokeys.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    so_subscription_count = fields.Integer(
        string='Sale Subscriptions', compute='_so_subscription_count')


    def _so_subscription_count(self):
        """ Compute the  number of subscription(s) """
        for partner in self:
            partner.so_subscription_count = self.env[
                'sale.subscription'].search_count([('partner_id', "=", partner.id)])


    def sale_subscription_action_res_partner(self):
        """ Action on click on the stat button in partner form """
        for partner in self:
            return {
                "type": "ir.actions.act_window",
                "res_model": "sale.subscription",
                "views": [[False, "tree"], [False, "form"]],
                "domain": [["partner_id", "=", partner.id]],
                "context": {"create": False},
                "name": "Sale Subscriptions",
            }
