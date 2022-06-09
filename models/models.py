# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, timedelta, time
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError, Warning
import urllib.parse
import requests
import math


class ResPartner(models.Model):
    _inherit = "res.partner"

    curp = fields.Char(string='CURP', help='Clave Única de Registro de Población')
    id_no = fields.Char(string='INE', help="INE o Número de identificación")
    ocupation = fields.Many2one(comodel_name="res.partner.industry",
                                string="Actividad",
                                help="Ocupación, Profesión, Actividad ó giro del negocio al que se dedique el cliente")
    foreign = fields.Selection([('res', 'Reside en el extranjero'),
                                ('nac', 'Nacido en el extranjero'),
                                ('amb', 'Nació y reside en el extranjero'),],
                               string="Extranjero", help='Establece si una persona vive o nació en el extranjero')
    #Validación de documentos
    chk_vat = fields.Boolean(string='RFC')
    doc_vat = fields.Binary(string="RFC", help="Anexa el RFC en formato PDF")
    chk_cur = fields.Boolean(string='CURP')
    doc_vat = fields.Binary(string="CURP", help="Anexa el CURP en formato PDF")
    chk_ids = fields.Boolean(string='INE o Pasaporte')
    doc_vat = fields.Binary(string="INE o Pasaporte", help="Anexa el INE o Pasaporte en formato PDF")
    chk_act = fields.Boolean(string='Acta Constitutiva')
    doc_vat = fields.Binary(string="Acta Constitutiva", help="Anexa el Acta Constitutiva en formato PDF")
    chk_avi = fields.Boolean(string='Aviso de Incripción')
    doc_vat = fields.Binary(string="Aviso de Incripción", help="Anexa el Aviso de Incripción en formato PDF")
    chk_est = fields.Boolean(string='Estructura Accionaria')
    doc_vat = fields.Binary(string="Estructura Accionaria", help="Anexa el Estructura Accionaria en formato PDF")
    chk_org = fields.Boolean(string='Organigrama')
    doc_vat = fields.Binary(string="Organigrama", help="Anexa el Organigrama en formato PDF")

    #Validación
    chk_gob = fields.Boolean(string='Gobierno')
    chk_fid = fields.Boolean(string='Fideicomiso')
