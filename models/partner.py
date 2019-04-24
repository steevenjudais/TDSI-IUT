# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.mx.rfc import _name_blacklist

class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    employee_ref = fields.Char('employee_ref')
    device_ids = fields.One2many('device', 'partner_id', string = "appareil")
    room_id = fields.Many2one('room', string="pièce")
    
    @api.multi
    def effaceAppareils(self):
        
        for record in self:
            record.device_ids = None

        return True