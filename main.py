from mid.comandos import mid
from uppay.conexao import conectaUppay 

def mn():
   
   #get the last vend id in MID
   commands = mid() 
   id = commands.getUltimoID()
   
   if(id!=None):
    #get the new vends in uppay   
    cn = conectaUppay()
    vendas = cn.connect(str(id))
    
    #save in google storage
    
    #for v in vendas:
    #    print(v)
    
    print(id)

mn()