from odoo import api, fields, models

class Hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'Hospital'
    _rec_name = 'hosp_name'

    hosp_name = fields.Char(string='Hospital Name', required=True)
    hosp_type = fields.Selection([('hospital','Hospital'),
                                  ('multi','Multi-Hospital'),
                                  ('nursing','Nursing-Home'),
                                  ('clinic','Clinic'),
                                  ('community','Community-Health Center'),
                                  ('military','Military Medical Center'),
                                  ], string='Institution Type')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    hosp_phone = fields.Char(string='Hospital Phone')
    hosp_email = fields.Char(string='Hospital Email')
    hosp_address = fields.Char(string='Hospital Address')
    hosp_street = fields.Char(string='Street')
    hosp_street2 = fields.Char(string='Street-2')
    hosp_zip = fields.Char(string='Zip')
    hosp_city = fields.Char(string='City')
    hosp_state_id = fields.Many2one('res.country.state', string="State")
    hosp_country_id = fields.Many2one('res.country', string='Country')
    note = fields.Text(string='Note')
    image = fields.Image(string='Image', max_width=128, max_height=128)
