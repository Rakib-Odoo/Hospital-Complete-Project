from odoo import api, models, fields

class Buildings(models.Model):
    _name = 'hospital.building'
    _description = 'Buildings'
    _rec_name = 'building_name'

    building_name = fields.Char(string='Block', required=True)
    institution_id = fields.Many2one('hospital.hospital', string='Institution')
    note = fields.Text(string='Note')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    bed_count = fields.Integer(string='Bed Count')
    ward_count = fields.Integer(string='Ward Count')