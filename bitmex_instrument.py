import bitmex
import threading
import settings
import sys
import datetime

class ExchangeInterface:
    def __init__(self):
        self.symbol = settings.SYMBOL
        self.bitmex = bitmex.bitmex(api_key=settings.API_KEY, api_secret=settings.API_SECRET, test=False)
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    

    def fetch_open_interest(self):
    	results = self.bitmex.Instrument.Instrument_get(symbol=self.symbol).result()
    	threading.Timer(settings.LOOP_INTERVAL, self.fetch_open_interest).start()

    	for result in results[0]:
            file = open(f'{self.current_date}.txt', "a")

            file.write(str(f'{result["openInterest"]}\n'))

def run():
    om = ExchangeInterface()
    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
       	om.fetch_open_interest()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    
if __name__== "__main__":
  run()