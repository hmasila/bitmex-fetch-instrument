import bitmex
import time

from config import *

from strategy import Strategy
from trader import Trader

client = bitmex.bitmex(
    test=TEST_EXCHANGE,
    api_key=API_KEY,
    api_secret=API_SECRET
)

strategy = Strategy(client, timeframe=TIMEFRAME)
trader = Trader(client, strategy, money_to_trade=AMOUNT_MONEY_TO_TRADE, leverage=LEVERAGE)

while True:
    if round(time.time()) % 2 == 0:
        trader.execute_trade()
        time.sleep(2)