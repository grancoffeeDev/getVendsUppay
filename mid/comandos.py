import requests

class mid:
    
    def __init__(self) -> None:
        pass
    
    def getUltimoID(self):
        url = "http://api.grancoffee.com.br:8000/mid/gc_config?id=eq.1"
        payload={}
        headers = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGlhY2Nlc3MifQ.BlvnsLa4kDAAlyxYuLRc1qo-hd72YqHPdr3SKnCxxqI'}
        response = requests.request("GET", url, headers=headers, data=payload)
        id = response.json()[0]['last_vendid']
        return id