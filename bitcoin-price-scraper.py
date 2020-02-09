import requests
import time


def scrape():
    response=requests.get(URL+COIN)
    response_json=response.json()
    return float(response_json[0]['price_usd'])


def last_update():
    response=requests.get(URL+COIN)
    response_json=response.json()
    return time.strftime('%a, %d %b %Y %H:%M:%S %Z',time.localtime(int((response_json[0]['last_updated']))))

URL='https://api.coinmarketcap.com/v1/ticker/'
COIN='bitcoin'
last_price=None

while True:
    latest_price=scrape()
    if latest_price!=last_price:
        print('latest price: ', latest_price)
        print(last_update())
        last_price=last_update()

