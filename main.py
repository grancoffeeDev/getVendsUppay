from models.parametros import parametros
import psycopg2

class main:
    
    def __init__(self) -> None:
        pass
    
    def teste(self):
        conn = psycopg2.connect(
            host="35.247.217.164",
            database="grancoffee",
            user="postgres",
            password="VnBgPQbYzwa95VDm")
        

a = main()
a.teste()