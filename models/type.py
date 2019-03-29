# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class type(models.Model):
    _name = 'type'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Le nom existe déjà')
    ]
    
    name = fields.Char('name', required = True)
    models_ids = fields.Many2many('models', string = 'Modèle')