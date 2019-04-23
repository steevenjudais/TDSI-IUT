#! /usr/bin/env python3

import csv
import erppeek
#client = erppeek.Client.from_config('test')
client = erppeek.Client("http://localhost:8071", "odoo", "judais1998.steeven@hotmail.fr", "rtlry")
appareils = client.Device
marques = client.Brand
types = client.Type
modeles = client.Models
employes = client.ResPartner
premiereLigne = True
numCol = 1
colonne = 8
colNom = "name"
colNumeroSerie = "serial_number"
colDateAllocation = "date_allocation"
colDateAchat = "date_purchase"
colModele = "model_id"
colMarque = "brand_id"
colType = "type_ids"
colEmploye = "partner_id"

nom = None
numeroSerie = None
dateAllocation = None
dateAchat = None
modele = ""
marque = None
type = None
employe = None

print("1,1,05/04/2019,01/04/2019,Samsung Galaxy Million,Samsung,Smartphone,Agrolait")

with open('devices.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if premiereLigne == True:
            #print(x)
            premiereLigne = False
        else:
            print({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},)
            nom = row[0]
            numeroSerie = row[1]
            dateAllocation = row[2]
            dateAchat = row[3]
            modele = row[4]
            marque = row[5]
            type = row[6]
            employe = row[7]
            
            if not types.search([(colNom,'=',type)]):
                types.create({colNom: type})
                
            if not marques.search([(colNom,'=',marque)]):
                marques.create({colNom: marque})
            
            pointeurType = types.search([(colNom,'=',type)])
            pointeurMarque = marques.search([(colNom,'=',marque)])
            
            if not modeles.search([(colNom,'=',modele)]):
               modeles.create({colNom: modele, "type_ids": [pointeurType[0]], "brand_id": pointeurMarque[0]})
                
            pointeurModele = modeles.search([(colNom,'=',modele)])
            
            if not employes.search([("name",'=',employe)]):
                if not appareils.search([(colNumeroSerie,'=',numeroSerie)]):
                    appareils.create({colNom: nom, colNumeroSerie: numeroSerie, colDateAllocation: dateAllocation, colDateAchat: dateAchat, colModele: pointeurModele[0]})
                    pointeurAppareil = appareils.search([(colNom,'=',nom)])
                    employes.create({colNom: employe, "device_ids": [pointeurAppareil[0]]})
                    #pointeurEmploye = employes.search([("name",'=',employe)])
                    #pointeurEmploye2 = '"' + pointeurEmploye[0] + '"'
                    #appareils.write({colEmploye: pointeurEmploye2})
            else:
                pointeurEmploye = employes.search([("name",'=',employe)])
                appareils.create({colNom: nom, colNumeroSerie: numeroSerie, colDateAllocation: dateAllocation, colDateAchat: dateAchat, colModele: pointeurModele[0], colEmploye: pointeurEmploye[0]})
            
                
                
                
                
                
                
                
                
                
                
                
                
                