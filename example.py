import logging
from kiteconnect import KiteTicker
from access_token import AccessTokenURI, Readwritejson

logging.basicConfig(level=logging.DEBUG)

access_token = Readwritejson.generateNewAccessToken()
api_key='api_key'
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
# margins
# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
