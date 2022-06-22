# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def cancel_old_quotations(self):
        records = self.env["sale.order"].search([])
        # expiration_records = [rec for rec in records if rec.validity_date] #records that have an expiration date
        # if not expiration_records: return

        today = fields.Date.today()
        # print(f"\n\n\nCancelling quotations at {today}\n\n\n")
        old_quotations = records.filtered(lambda r: r.validity_date).filtered(lambda r: r.validity_date < today) #
        # for oq in old_quotations: print(f"{oq.name} cancelled"); print("\n\n")
        return old_quotations.write({
            'state': 'cancel',
        })