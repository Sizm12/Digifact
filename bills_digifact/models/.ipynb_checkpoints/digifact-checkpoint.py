from odoo import models, fields, api

class Invoice Digifact(models.Model):
    _inherit='account.move'
    
    def test_button_function(self):
        print('Prueba de Boton')