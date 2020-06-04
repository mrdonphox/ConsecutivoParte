# -*- coding: utf-8 -*-
from odoo import models, fields,api, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ProdCons = fields.Char(string='Id único', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('ProdCons', _('New')) == _('New'):
            vals['ProdCons'] = self.env['ir.sequence'].next_by_code('product.dolmen.sequence') or _('New')
        result = super(ProductTemplate, self).create(vals)
        return result
