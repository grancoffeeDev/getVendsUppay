import psycopg2
from uppay.config import config
#from config import config

class conectaUppay:
    def connect(self, id):
    
        conn = None
        vendas = None
        
        try:
            
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('select * from gc_vends gv where id >'+id)
            vendas = cur.fetchall()
            
            #for v in vendas:
            #    print(v)
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
        return vendas

#if __name__ == '__main__':
#a = conectaUppay()
#a.connect("3541137")