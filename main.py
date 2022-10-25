from mid.comandos import mid
from uppay.conexao import conectaUppay 
from uteis.util import util
from google.googlestorage import GCStorage
import json

def mn():
   
   #get the last vend id in MID
   commands = mid() 
   id = commands.getUltimoID()
   print(id)
   
   if(id!=None):
    #get the new vends in uppay   
    cn = conectaUppay()
    vendas = cn.connect(str(id))
    
    #save in google storage
    gcs = GCStorage()
    gcs.enviaDados(vendas)

mn()