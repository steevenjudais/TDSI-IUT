# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class brand(models.Model):
    _name = 'brand'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Le nom existe déjà')
    ]
    
    name = fields.Char('name', required = True)
    warranty_delay_month = fields.Integer('warranty_delay_month')
    support_phone = fields.Integer('support_phone')