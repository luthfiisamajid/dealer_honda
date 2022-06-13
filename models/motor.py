from odoo import api, fields, models

class motor(models.Model):
    _name = 'dealer_honda.motor'
    _description = 'Type Motor'

    name = fields.Char(string='Name')
    harga = fields.Integer(string='Harga')
    stok = fields.Char(string='Stok')
    jenis_id = fields.Many2one(comodel_name='dealer_honda.jenis', string='Jenis')
    
    
    
