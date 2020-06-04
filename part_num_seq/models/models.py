# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class part_num_seq(models.Model):
#     _name = 'part_num_seq.part_num_seq'
#     _description = 'part_num_seq.part_num_seq'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
