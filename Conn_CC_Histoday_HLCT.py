
import urllib.request
import json
import requests

# Documentation
# https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistohour&api_key=0790f87f52c4f2eefe094943d95f1fd321cd4eb4d746cd02d61673856afdb1c4
# Visor JSON elements  http://jsonviewer.stack.hu/


def getTokenToFiat_sin_key(token, fiat, limit):
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={a}&tsym={b}&limit={c}&api_key={d}'.format(
        a=token, b=fiat, c=limit, d=apiKey)
    result = requests.get(url).json()
    # response = urllib.request.urlopen(url)
    # data = json.loads(response.read())
    print(result['Data'][1]['low'])


getTokenToFiat_sin_key('BTC', 'USD', 10)
# https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=10&api_key=0790f87f52c4f2eefe094943d95f1fd321cd4eb4d746cd02d61673856afdb1c4


def getTokenToFiat_con_key(token, fiat):
    apiKey = "0790f87f52c4f2eefe094943d95f1fd321cd4eb4d746cd02d61673856afdb1c4"

    url = "https://min-api.cryptocompare.com/data/price"
    payload = {
        "fsym": token,
        "tsyms": fiat
    }
    headers = {
        "authorization": "Apikey " + apiKey
    }
    result = requests.get(url, headers=headers, params=payload).json()

    print(result)


getTokenToFiat_con_key('BTC', 'USD')
