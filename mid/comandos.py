import requests
import json

class mid:
    
    def __init__(self) -> None:
        self.token = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGlhY2Nlc3MifQ.BlvnsLa4kDAAlyxYuLRc1qo-hd72YqHPdr3SKnCxxqI'}
        pass
    
    def getUltimoID(self):
        url = "http://api.grancoffee.com.br:8000/mid/gc_config?id=eq.1"
        payload={}
        response = requests.request("GET", url, headers=self.token, data=payload)
        id = response.json()[0]['last_vendid_teste']
        return id
    
    def salvaVendasMID(self, vendas):
        url = "http://api.grancoffee.com.br:8000/mid/gc_movimentacao_teste"
        for v in vendas:
            requests.post(url, data=json.dumps(v), headers=self.token)
            