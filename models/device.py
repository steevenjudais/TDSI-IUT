# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class device(models.Model):
    _name = 'device'
    
    name = fields.Char('name', required = True)
    date_allocation = fields.Char('date_allocation')
    serial_number = fields.Char('serial_number', required = True)
    date_purchase = fields.Date('date_purchase')
    date_warranty_end = fields.Date('date_warranty_end')