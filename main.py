from mid.comandos import mid
from uppay.conexao import conectaUppay 
from uteis.util import util
from google.googlestorage import GCStorage
import json
import functions_framework

@functions_framework.cloud_event
def mn(cloud_event=None):
   
   #get the last vend id in MID
   commands = mid() 
   id = commands.getUltimoID()
   print(id)
   
   if(id!=None):
    #get the new vends in uppay   
    cn = conectaUppay()
    vendas = cn.connect(str(id))
    v = json.loads(vendas)
    
    #convert json to jsonl
    u = util()
    vendasL = u.json2jsonl(v)
    
    #save in google storage
    gcs = GCStorage(str(id))
    gcs.enviaDados(vendasL)
    
    #save in MID
    commands.salvaVendasMID(v)
    
    return

#mn()