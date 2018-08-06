from os.path import join
import logging

########################################################################################################################
# Connection/Auth
########################################################################################################################

# API URL.
BASE_URL = "https://testnet.bitmex.com/api/v1/"
# BASE_URL = "https://www.bitmex.com/api/v1/" # Once you're ready, uncomment this.

# The BitMEX API requires permanent API keys. Go to https://testnet.bitmex.com/api/apiKeys to fill these out.
API_KEY = ""
API_SECRET = ""
TEST_EXCHANGE = False



########################################################################################################################
# Target
########################################################################################################################

# Instrument to market make on BitMEX.
SYMBOL = "XBTUSD"

# How often to re-check and fetch instrument details.
# Generally, it's safe to make this short
LOOP_INTERVAL = 5

# Available levels: logging.(DEBUG|INFO|WARN|ERROR)
LOG_LEVEL = logging.INFO

# Specify the contracts that you hold. These will be used in portfolio calculations.
CONTRACTS = ['XBTUSD']

AMOUNT_MONEY_TO_TRADE=100 #$
LEVERAGE=5

TIMEFRAME = '1d'

time_to_wait_new_trade = {'1m': 60,
                          '5m': 60*5,
                          '1h': 60*60,
                          '1d': 60*60*24}
