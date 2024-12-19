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
                                  default=lambda self: self.env.ref('base.BDT').id, required=True)
    repair_charge = fields.Float(string='Repair Charge', help='The repairing charge whether any damage is happened',currency_field='currency_id')
    bed_rent = fields.Float(string='Bed Rent', help='The charge for the bed', currency_field='currency_id')
    repair_date = fields.Date(string='Repair Date', help='The next repairing date.')
    ward_id = fields.Many2one('hospital.ward', string='Ward No')
    institution_id = fields.Many2one('hospital.hospital',string='Institution')
    building_id = fields.Many2one('hospital.building', string='Block')

    state = fields.Selection([('available','Available'),
                              ('unavailable','Unavailable')
                              ], string='Status')


    @api.onchange('institution_id')
    def _onchange_ward_bed(self):
        return {
            'domain': {
                'building_id' : [
                    ('institution_id', '=', self.institution_id.id),
                ]}}

    @api.onchange('building_id')
    def _onchange_ward(self):
        return {
            'domain': {
                'ward_id': [
                    ('building_id', '=', self.building_id.id),
                ]
            }
        }

    def action_available(self):
        self.state = 'available'

    def action_unavailable(self):
        self.state = 'unavailable'