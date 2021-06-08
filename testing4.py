# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RecCompany(models.Model):
    _inherit = "res.company"

    fb_page_id = fields.Char("Facebook Page ID")
    fb_theme_color = fields.Char("Chat Color")
    fb_logged_in_greeting = fields.Char("Logged In Message")
    fb_logged_out_greeting = fields.Char("Logged Out Message")
