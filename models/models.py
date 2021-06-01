# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class HmsDepartment(models.Model):
    _name = 'hms.department'
    _description = 'hospital__managment__system.hospital__managment__system'

    name = fields.Char()
    capacity = fields.Integer()
    is_opend = fields.Boolean()
    patients_id = fields.One2many('hms.patients', 'department_id')

    @api.onchange('is_opend')
    def on_change(self):
        # self.float = self.value / 3
        # if self.is_opend:
             raise ValidationError('value 2 must be less than 200')

class HmsDoctor(models.Model):
    _name = 'hms.doctors'
    _description = 'This is Doctors'
    _rec_name = 'fname'

    fname = fields.Char()
    lname = fields.Char()
    image = fields.Binary()

class HmsPatient(models.Model):
    _name = 'hms.patients'
    _description = 'hThis is patients'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'fname'

    department_id = fields.Many2one('hms.department', 'Department Name')
    dep_capacity = hms.department.capacity

#
    fname = fields.Char(string='First Name',  default='Ahmed')
    lname = fields.Char(string='Last Name')
    date_of_birth = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [('a', 'A'), ('b', 'B'), ('o', 'O'), ('ab', 'AB')], default='a')
    state = fields.Selection(
        [('undetermined', 'Undetermined'), ('good', 'Good'), ('fair', 'Fair'), ('serious', 'Serious')], default='undetermined', tracking=True)

    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()




