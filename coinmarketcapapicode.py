import requests
from requests import Session
import secrets
from pprint import pprint

#https://coinmarketcap.com/api/documentation/v1/

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.api_key,
}

#testing
r = requests.get(url, headers=headers)
print(r.status_code)
#pprint(r.json())
#alright till here------------


class CMC:
    def __init__(self, token):
        self.api_url = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    def getallcoins(self):
        self.url = self.api_url + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data
    
    def get_meta_data(self, slug):
        self.url = self.api_url + '/v2/cryptocurrency/info'
        r = self.session.get(url)
        parameters = {'slug': slug}
        data = r.json()['data']
        return data

cmc = CMC(secrets.api_key)

pprint(cmc.get_meta_data('bitcoin'))