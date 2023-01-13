from odoo import models, fields, api

class account_move_inherit(models.Model):
    _inherit='account.move'
    
    def test_button_function(self):
        raise Warning('Prueba de Boton')