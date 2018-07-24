import bitmex
import threading
import settings
import sys
import datetime
from time import sleep
from web_socket_thread import BitMEXWebsocket

class ExchangeInterface:
    def __init__(self):
        self.symbol = settings.SYMBOL
        self.bitmex = bitmex.bitmex(api_key=settings.API_KEY, api_secret=settings.API_SECRET, test=False)
        self.ws = BitMEXWebsocket()
        self.ws.connect(settings.BASE_URL, self.symbol)

    def fetch_open_interest(self):
    	res = self.bitmex.Instrument.Instrument_get(symbol=self.symbol).result()
    	threading.Timer(settings.LOOP_INTERVAL, self.fetch_open_interest).start()

    	for n in res[0]:
    		print(n)

    #
    # Public methods
    #

    def instrument(self):
        """Get an instrument's details."""
        return self.ws.get_instrument(self.symbol)

    def __del__(self):
        self.exit()

    def exit(self):
        self.ws.exit()

def run():
    om = ExchangeInterface()
    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
    	# while True:
        	# print(om.instrument())
        	# sleep(settings.LOOP_INTERVAL)
       	om.fetch_open_interest()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    
if __name__== "__main__":
  run()