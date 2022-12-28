import psycopg2
from uppay.config import config
#from config import config
import json
from datetime import date, datetime
from psycopg2.extras import RealDictCursor

class conectaUppay:
    
    def __init__(self) -> None:
        pass
    
    def json_serial(obj):

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))
    
    
    def connect(self, id):
    
        conn = None
        vendas = None
        final_json = {}
        
        try:
            
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute('select '+
                'id as id_item, '+
                'dt_mov, '+
                'coalesce(sankhya_id,\'VAZIO\') as codbem, '+
                'tecla::varchar, '+
                'coalesce(codprod,\'0\') as codprod, '+
                '2 as id_telemetria, '+
                'id_mov, '+
                'qtd as quantidade, '+
                'valor, '+
                '\'V\' as tipmov, '+
                'case when status=\'2\' and movimento=-1 then -1 else 0 end as movimento, '+
                'status, '+
                'message, '+
                'gateway, '+
                'brand, '+
                'request_number, '+
                'customer_uuid, '+
                'embedded_charging, '+
                'statusvenda, '+
                'moderninha, '+
                'tipo, '+
                'user_uid, '+
                'glocation, '+
                'user_agent, '+
                'user_ip, '+
                'current_timestamp as dt_inc, '+
                'user_name, '+
                'cashback, '+
                'case when cashback=true then coalesce((valor::float*reward_percent::float)/100::integer,0) else 0 end as cashback_value, '+
                'case when cashback=false and (reward_percent > 0 or reward_amount > 0) then true else false end as discount, '+
                'case when cashback=false and reward_percent > 0 then coalesce((valor::float*reward_percent::float)/100::integer,0) else 0 end as discount_value, '+
                'cardnumber, '+
                'qrcode '
                'from gc_vends gv where id >'+id+
                ' and id < 3740429 order by id')
            vendas = json.dumps(cur.fetchall(),indent=4, default=conectaUppay.json_serial)
            
            if(vendas!=None):
                final_json = vendas
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
        return final_json

#if __name__ == '__main__':
#a = conectaUppay()
#a.connect("3573971")