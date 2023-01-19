from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests
import elementpath
import xml.etree.ElementTree as xml

class account_move_inherit(models.Model):
    _inherit='account.move'
    
    def validar_factura_electronica_facturacion(self):
        
        for rec in self:
            
            for item in rec.invoice_line_ids:
                tax= item.tax_ids.amount
                product= item.product_id.name
                quantity= item.quantity
                price= item.price_unit
                taxs= price * tax
                total_product= (price+taxs)*quantity
                response= product +"-"+ total_product
                raise UserError(_('El producto es %s'%response)) 
            
            #root= xml.Element("dte:GTDocumento", {'xmlns:xsi':"http://www.w3.org/2001/XMLSchema-instance", 'xmlns:dte':"http://www.sat.gob.gt/dte/fel/0.2.0", 'Version':"0.1"})

            #tree= xml.tostring(root, encoding='utf8', method='xml', xml_declaration=True)
            
            
            
            #customer = rec.partner_id.name
            
            #for item in rec.invoice_line_ids:
                #var= item.product_id.name
            #raise UserError(_('El cliente es %s'%var)) 

        #URL= "https://felgttestaws.digifact.com.gt/gt.com.fel.api.v3/api/login/get_token"
        #Params={"Username":"GT.000041545036.TESTUSER","Password":"j6C7&f5?"}
        #response= requests.post(url=URL, data=Params)
        #raise UserError(_('Peticion a Digifact is %s'%response.text))