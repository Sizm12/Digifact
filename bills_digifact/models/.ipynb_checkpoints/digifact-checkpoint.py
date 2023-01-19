from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests
import xml.etree.ElementTree as xml

class account_move_inherit(models.Model):
    _inherit='account.move'
    
    def validar_factura_electronica_facturacion(self):
        
        for rec in self:
            
            root= xml.Element("dte:GTDocumento", {'xmlns:xsi':"http://www.w3.org/2001/XMLSchema-instance", 'xmlns:dte':"http://www.sat.gob.gt/dte/fel/0.2.0", 'Version':"0.1"})
            f1= xml.SubElement(root, "dte:SAT",{'ClaseDocumento':"dte"})
            f11 = xml.SubElement(f1, "dte:DTE", {'ID':"DatosCertificados"})
            f2= xml.SubElement(f11, "dte:DatosEmision", {'ID':"DatosEmision"})
            f31= xml.SubElement(f2, "dte:DatosGenerales", {'Tipo':"FACT", 'FechaHoraEmision': "2023-01-17T09:20:00", 'CodigoMoneda': "GTQ"})
            f32= xml.SubElement(f2, "dte:Emisor", {'NITEmisor':"41545036", 'NombreEmisor':"Nombre o Razon Social", 'CodigoEstablecimiento':"1", 'NombreComercial':"Nombre del establecimiento comercial", 'AfiliacionIVA':"GEN"})
            f321= xml.SubElement(f32, "dte:DireccionEmisor")
            f3211= xml.SubElement(f321, "dte:Direccion")
            f3211.text="Boulevard El Caminero 14-32, Zona 6 de Mixco"
            f3212= xml.SubElement(f321, "dte:CodigoPostal")
            f3212.text="01006"
            f3213=xml.SubElement(f321, "dte:Municipio")
            f3213.text="MIXCO"
            f3214=xml.SubElement(f321, "dte:Departamento")
            f3214.text="GUATEMALA"
            f3215=xml.SubElement(f321, "dte:Pais")
            f3215.text="GT"
            f33= xml.SubElement(f2, "dte:Receptor", {'NombreReceptor':"LILIA ORTIZ NIJ", 'CorreoReceptor':"sucorreo@gmail.com", 'IDReceptor':"CF"})
            f331= xml.SubElement(f33, "dte:DireccionReceptor")
            f3311= xml.SubElement(f331, "dte:Direccion")
            f3311.text="SECTOR 1 ESTANCIA DE LA VIRGEN"
            f3312= xml.SubElement(f331, "dte:CodigoPostal")
            f3312.text="01006"
            f3313=xml.SubElement(f331, "dte:Municipio")
            f3313.text="MIXCO"
            f3314=xml.SubElement(f331, "dte:Departamento")
            f3314.text="GUATEMALA"
            f3315=xml.SubElement(f331, "dte:Pais")
            f3315.text="GT"
            f34=xml.SubElement(f2, "dte:Frases")
            f341=xml.SubElement(f34, "dte:Frase", {'TipoFrase':"1", 'CodigoEscenario':"1"})
            Items=xml.SubElement(f2, "dte:Items")
            Item= xml.SubElement(Items,'dte:Item', {'NumeroLinea':"1", 'BienOServicio':"B"})
            Cantidad= xml.SubElement(Item, 'dte:Cantidad')
            Cantidad.text= "1"
            UnidadMedida= xml.SubElement(Item, 'dte:UnidadMedida')
            UnidadMedida.text= "CA"
            Descripcion= xml.SubElement(Item, 'dte:Descripcion')
            Descripcion.text= "Valvula"
            PrecioUnitario= xml.SubElement(Item, 'dte:PrecioUnitario')
            PrecioUnitario.text= "1"
            Precio= xml.SubElement(Item, 'dte:Precio')
            Precio.text= "1.0000"
            Descuento= xml.SubElement(Item, 'dte:Descuento')
            Descuento.text= "0"
            Impuestos =  xml.SubElement(Item, "dte:Impuestos")
            Impuesto = xml.SubElement(Impuestos, "dte:Impuesto")
            Nombre= xml.SubElement(Impuesto, "dte:NombreCorto")
            Nombre.text="IVA"
            CodigoUnidad= xml.SubElement(Impuesto, "dte:CodigoUnidadGravable")
            CodigoUnidad.text="1"
            MontoGravable = xml.SubElement(Impuesto, "dte:MontoGravable")
            MontoGravable.text = "0.89286"
            MontoImpuesto = xml.SubElement(Impuesto, "dte:MontoImpuesto")
            MontoImpuesto.text = "0.10714"
            Total =  xml.SubElement(Item, "dte:Total")
            Total.text = "1.0000"    
            f36=xml.SubElement(f2, "dte:Totales")
            TotalImpuestos= xml.SubElement(f36, "dte:TotalImpuestos")
            TotalImpuesto= xml.SubElement(TotalImpuestos, "dte:TotalImpuesto", {'NombreCorto': "IVA", 'TotalMontoImpuesto':"0.10714"})
            GranTotal= xml.SubElement(f36, "dte:GranTotal")
            GranTotal.text= "1.0000"   

            tree= xml.tostring(root, encoding='utf8', method='xml', xml_declaration=True)
            raise UserError(_('La consulta es %s'%tree)) 
            
            
            #customer = rec.partner_id.name
            
            #for item in rec.invoice_line_ids:
                #var= item.product_id.name
            #raise UserError(_('El cliente es %s'%var)) 

        #URL= "https://felgttestaws.digifact.com.gt/gt.com.fel.api.v3/api/login/get_token"
        #Params={"Username":"GT.000041545036.TESTUSER","Password":"j6C7&f5?"}
        #response= requests.post(url=URL, data=Params)
        #raise UserError(_('Peticion a Digifact is %s'%response.text))