from odoo import api, fields, models


class Beds(models.Model):
    _name = 'hospital.bed'
    _description = 'Beds'
    _rec_name = 'bed_no'

    bed_no = fields.Char(string='Bed No', required=True)
    bed_type = fields.Selection([('general', 'General'),
                                 ('icu', 'ICU'),
                                 ('vip', 'VIP'),
                                 ], string='Bed Type')
    note = fields.Text(string='Notes')
    date_bed_assign = fields.Date(string='Bed Assign Date', default=fields.Date.today)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    repair_charge = fields.Monetary(string='Repair Charge', help='The repairing charge whether any damage is happened')
    bed_rent = fields.Monetary(string='Bed Rent', help='The charge for the bed')
    repair_date = fields.Date(string='Repair Date', help='The next repairing date.')
