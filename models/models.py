# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

# class tdsimodel(models.Model):
#     _name = 'tdsimodel.tdsimodel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class models(models.Model):
    _name = 'models'
    _sql_constraints = [
        ('ref_uniq', 'unique (ref)', 'La référence existe déjà')
    ]
    
    name = fields.Char('name', required = True)
    ref = fields.Char('ref')
    type_ids = fields.Many2many('type', string = "Type")
    brand_id = fields.Many2one('brand', string= "marque")
    device_ids = fields.One2many('device', 'model_id', string = "appareil")
    
    