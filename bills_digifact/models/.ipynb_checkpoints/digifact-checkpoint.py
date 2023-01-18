from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests

class account_move_inherit(models.Model):
    _inherit='account.move'
    
    def test_button_function(self):
        
        for rec in self:
            customer = rec.partner_id.name
            
            for item in rec.invoice_line_ids:
                var= item.product_id.name
                raise UserError(_('El cliente es %s'%var)) 

        #URL= "https://felgttestaws.digifact.com.gt/gt.com.fel.api.v3/api/login/get_token"
        #Params={"Username":"GT.000041545036.TESTUSER","Password":"j6C7&f5?"}
        #response= requests.post(url=URL, data=Params)
        #raise UserError(_('Peticion a Digifact is %s'%response.text))