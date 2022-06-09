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

    #Validación
    chk_gob = fields.Boolean(string='Gobierno', help='Establece si una Persona Física o Moral pertenece al Gobierno')
    chk_fid = fields.Boolean(string='Fideicomiso', help='Establece si una Persona Física o Moral pertenece a un Fideicomiso')

    #Validación de documentos
    name_vat = fields.Char(string='RFC')
    chk_vat = fields.Boolean(string='RFC', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_vat = fields.Binary(string="RFC", help="Anexa el RFC en formato PDF")

    name_cur = fields.Char(string='CURP')
    chk_cur = fields.Boolean(string='CURP', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_cur = fields.Binary(string="CURP", help="Anexa el CURP en formato PDF")

    name_ids = fields.Char(string='INE o Pasaporte')
    chk_ids = fields.Boolean(string='INE o Pasaporte', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_ids = fields.Binary(string="INE o Pasaporte", help="Anexa el INE o Pasaporte en formato PDF")

    name_act = fields.Char(string='Acta Constitutiva')
    chk_act = fields.Boolean(string='Acta Constitutiva', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_act = fields.Binary(string="Acta Constitutiva", help="Anexa el Acta Constitutiva en formato PDF")

    name_avi = fields.Char(string='Aviso de Incripción')
    chk_avi = fields.Boolean(string='Aviso de Incripción', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_avi = fields.Binary(string="Aviso de Incripción", help="Anexa el Aviso de Incripción en formato PDF")

    name_est = fields.Char(string='Estructura Accionaria')
    chk_est = fields.Boolean(string='Estructura Accionaria', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_est = fields.Binary(string="Estructura Accionaria", help="Anexa el Estructura Accionaria en formato PDF")

    name_org = fields.Char(string='Organigrama')
    chk_org = fields.Boolean(string='Organigrama', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_org = fields.Binary(string="Organigrama", help="Anexa el Organigrama en formato PDF")

    name_dec = fields.Char(string='Declaración Firmada')
    chk_dec = fields.Boolean(string='Declaración Firmada', help='Marque la siguiente casilla si el cliente entregó el siguiente documento')
    doc_dec = fields.Binary(string="Declaración Firmada", help="Anexa la Declaración Firmada en formato PDF")

    #Ubicaciones
    operation_state = fields.Many2one(comodel_name='res.country.state', string='Entidad de Operación', ondelete='restrict')
    operation_country = fields.Many2one(comodel_name='res.country', string='País de Operación', ondelete='restrict')

    operation_state_id = fields.Many2one(comodel_name='res.country.state', string='Entidad de Operación', ondelete='restrict')
    operation_country_id = fields.Many2one(comodel_name='res.country', string='País de Operación', ondelete='restrict')