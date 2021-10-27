# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Medicine(models.Model):
     _name = 'custom_module_name.medicine'
     _description = 'medicine models'

     name = fields.Char()
     description = fields.Text()
     usage_type = fields.Char()
     barcode = fields.Char()
     sale_price = fields.Float()
     scientific_name = fields.Char()
     originator = fields.Char(string="Company")
     moves = fields.One2many(comodel_name='custom_module_name.moves', inverse_name='medicine')
     quantity_available = fields.Float(compute='_get_quantity', store=True)

     @api.depends("moves")
     def _get_quantity(self):
          for record in self:  # [1, 2, ....n]
               # total = 0.0
               # Method {1}
               # moves_items = self.env['os21.pharmacy.moves'].search([('medicine', '=', record.id)])
               # for move in moves_items:
               #     total += move.quantity
               # Method {2}
               # for move in record.moves:
               #     total += move.quantity
               # Method {3}
               record.quantity_available = sum(record.moves.mapped('quantity'))


     class MedicineMoves(models.Model):
          _name = 'custom_module_name.moves'
          _description = 'Medicine Moves'

          name = fields.Char()
          quantity = fields.Float()
          timestamp = fields.Datetime()
          medicine = fields.Many2one(comodel_name='custom_module_name.medicine')










#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
