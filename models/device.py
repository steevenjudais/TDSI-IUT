# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist
from datetime import *; from dateutil.relativedelta import *
import calendar

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
    
    @api.onchange('date_purchase')
    def check_change(self):
        brand = self.env['brand'].search([('id','=',self.model_id.brand_id.id)])
        dateAjout = brand.warranty_delay_month
        TODAY = date.today()
        
        if self.date_purchase != False:
            dateVrai = fields.Date.from_string(self.date_purchase) + relativedelta(months=+dateAjout)
            self.date_warranty_end = dateVrai
        else:
            dateVrai = TODAY + relativedelta(months=+dateAjout)
            self.date_warranty_end = dateVrai
            self.date_purchase = TODAY
    
    @api.one
    def coche(self):   
        if self.availaible == True:
            self.write({'date_allocation': ""})
        self.write({'availaible': not self.availaible})
        return True
    