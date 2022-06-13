from odoo import api, fields, models

class jenis(models.Model):
    _name = 'dealer_honda.jenis'
    _description = 'Jenis Motor'

    name = fields.Char(string='Name')
    transmisi = fields.Char(string='Transmisi')
    kapasitasoli = fields.Char(string='Kapasitas Oli')
    
