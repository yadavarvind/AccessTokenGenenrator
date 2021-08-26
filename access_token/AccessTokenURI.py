#!python
import logging
import requests
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_key='api_key'
zerodha_id = 'zerodha_id'
zerodha_password = 'zerodha_password'
zerodha_pin = 'zerodha_pin'
api_secret = 'api_secret'

def getAccessToken():
    kite = KiteConnect(api_key=api_key)


    url = kite.login_url()
    # print(url)
    login = requests.get(url)
    
    cookies = ';'.join([f'{k}={v}' for k, v in login.history[1].cookies.items()])
    # print(cookies)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
        "X-Kite-Userid": zerodha_id, 'X-Kite-Version': '2.4.0',
        'Cookie': cookies, 'Referer': login.url
    }

    data = requests.post('https://kite.zerodha.com/api/login', data={'user_id': zerodha_id, 'password': zerodha_password},
                         headers=headers)

    request_id = data.json()['data']['request_id']
    data = requests.post('https://kite.zerodha.com/api/twofa',
                         data={'user_id': zerodha_id, 'request_id': request_id, 'twofa_value': zerodha_pin}, headers=headers)


    token = ';'.join([f'{k}={v}' for k, v in data.cookies.items()])

    enctoken = token.split(';')[1][9:]
    return enctoken


