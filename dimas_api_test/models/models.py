from odoo import fields,models
from odoo.tools.translate import html_translate
from odoo import api, fields, models, tools, _

class DimasKampus(models.Model):
    _name = 'dimas.kampus'
    _description = 'kampus Dimas'

    name = fields.Char('Nama Kampus')
    jenis_kampus = fields.Selection(
        selection=[
            ('swasta', 'Swasta'),
            ('negeri', 'Negeri'),
        ]
    )
    akreditasi = fields.Selection(
        selection=[
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
            ('unggul', 'Unggul'),
            ('baik', 'Baik'),
            ('baik_sekali', 'Baik Sekali'),
            ('tidak_terakreditasi', 'Tidak Terakreditasi'),
        ]
    )
    status = fields.Char('status')
    no_telp = fields.Char('Nomor Televon')
    fax = fields.Char('fax')
    alamat = fields.Char('alamat')

class DimasJurusan(models.Model):
    _name = 'dimas.jurusan'
    _description = 'jurusan Dimas'

    name = fields.Char('Nama jurusan')
    akreditasi = fields.Selection(
        selection=[
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
            ('unggul', 'Unggul'),
            ('baik', 'Baik'),
            ('baik_sekali', 'Baik Sekali'),
            ('tidak_terakreditasi', 'Tidak Terakreditasi'),
        ]
    )
    name_kampus_ids = fields.Many2one(string="Campus Asal",comodel_name='dimas.kampus')

class DimasFollowKampus(models.Model):
    _name = 'dimas.follow.kampus'
    _description = ' Dimas follow kampus'

    name = fields.Many2one('res.users', string='Follow by', default=lambda self: self.env.user )
    name_kampus_ids = fields.Many2one(string="Campus Asal",comodel_name='dimas.kampus')
