# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class partner(models.Model):
    _name = 'partner'
    
    name = fields.Char('name', required = True)
    employee_ref = fields.Char('employee_ref')
    device_ids = fields.One2many('device', 'id', string = "appareil")