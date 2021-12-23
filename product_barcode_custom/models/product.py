# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"


    def ar_total_tax(self):
        if self.taxes_id:
              return self.list_price * 0.15

    def total_amount_tax(self):
        if self.taxes_id:
            list = self.list_price * 0.15
            # return self.list_price + list
            return self.env.user.company_id.currency_id.name + str(self.list_price + list)

    def company_name(self):
        return self.env.user.company_id.name




class ProductTemplate(models.Model):
    _inherit = "product.template"

    def ar_total_tax(self):
        if self.taxes_ids:
              return self.list_price * 0.15
    def total_amount_tax(self):
        if self.taxes_ids:
            list = self.list_price * 0.15
            return self.env.user.company_id.currency_id.name + str(self.list_price + list)

