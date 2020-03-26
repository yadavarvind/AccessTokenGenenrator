# AccessTokenGenenrator
Zerodha ( Kite ) access token generator

Provide details in AccessTokenURI your following details

api_key='api_key'                                            
zerodha_id = 'zerodha_id'                                      
zerodha_password = 'zerodha_password'                                                          
zerodha_pin = 'zerodha_pin'                                        
api_secret = 'api_secret'

Please check example for accessing Zerodha access_token


import logging
from kiteconnect import KiteTicker
from access_token import AccessTokenURI, Readwritejson

logging.basicConfig(level=logging.DEBUG)

access_token = Readwritejson.generateNewAccessToken()

kws = KiteTicker("api_key", access_token)

def on_ticks(ws, ticks):  # noqa
    # Callback to receive ticks.
    logging.info("Ticks: {}".format(ticks))

def on_connect(ws, response):  # noqa
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([3677697])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [3677697])

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()

