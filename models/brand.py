# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist
from datetime import *; from dateutil.relativedelta import *
import calendar

class brand(models.Model):
    _name = 'brand'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Le nom existe déjà')
    ]
    
    name = fields.Char('name', required = True)
    warranty_delay_month = fields.Integer('warranty_delay_month')
    support_phone = fields.Integer('support_phone')
    models_ids = fields.One2many('models', 'brand_id', string = "modèle")
    
    @api.one
    def majFinGarantie(self):
        
        TODAY = date.today()
        if self.warranty_delay_month > 0:
            dateAjout = self.warranty_delay_month
            
            devices = self.env['device'].search([('model_id.brand_id','=',self.id)])

            #dateVrai = TODAY + relativedelta(months=+dateAjout)
            #devicesSansDateAchat.write({'date_warranty_end': dateVrai})
            
            for chaque in devices:
                if chaque.date_purchase != False:
                    dateVrai = fields.Date.from_string(chaque.date_purchase) + relativedelta(months=+dateAjout)
                    chaque.date_warranty_end = dateVrai
                else:
                    dateVrai = TODAY + relativedelta(months=+dateAjout)
                    chaque.date_warranty_end = dateVrai
                    chaque.date_purchase = TODAY
        return True