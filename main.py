from mid.comandos import mid
from uppay.conexao import conectaUppay 

def mn():
   
   commands = mid() 
   id = commands.getUltimoID()
   if(id!=None):
    cn = conectaUppay()
    cn.connect(str(id))   
    print(id)

mn()