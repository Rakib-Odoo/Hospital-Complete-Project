from odoo import api, fields, models

class Wards(models.Model):
    _name = 'hospital.ward'
    _description = 'Wards'
    _rec_name = 'ward_no'


    ward_no = fields.Char(string='Ward Name', required=True)
    floor_no = fields.Integer(string='Floor No.')
    note = fields.Text(string='Notes')
    bed_count = fields.Integer(string='Bed Count')