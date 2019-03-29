# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class room(models.Model):
    _name = 'room'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Le nom existe déjà')
    ]
    
    name = fields.Char('name', required = True)
    floor = fields.Char('floor')