# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class device(models.Model):
    _name = 'device'
    _sql_constraints = [
        ('serial_number_uniq', 'unique (serial_number)', 'Le numéro de série existe déjà')
    ]
    
    name = fields.Char('name', required = True)
    date_allocation = fields.Char('date_allocation')
    serial_number = fields.Char('serial_number', required = True)
    date_purchase = fields.Date('date_purchase')
    date_warranty_end = fields.Date('date_warranty_end')
    partner_id = fields.Many2one('res.partner', string="partenaire")
    model_id = fields.Many2one('models', string="modèle")
    availaible = fields.Boolean('disponible')
    
    @api.one
    def coche(self):   
        if self.availaible == True:
            self.write({'date_allocation': ""})
        self.write({'availaible': not self.availaible})
        return True
    