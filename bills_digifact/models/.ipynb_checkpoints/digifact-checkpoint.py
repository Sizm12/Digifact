from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests

class account_move_inherit(models.Model):
    _inherit='account.move'
    
    def test_button_function(self):
        
        customer= self._fields['partner_id'].value
        raise UserError(_('El cliente es %s'%customer))
        #URL= "https://felgttestaws.digifact.com.gt/gt.com.fel.api.v3/api/login/get_token"
        #Params={"Username":"GT.000041545036.TESTUSER","Password":"j6C7&f5?"}
        #response= requests.post(url=URL, data=Params)
        #raise UserError(_('Peticion a Digifact is %s'%response.text))