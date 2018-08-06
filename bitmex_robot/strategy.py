import talib
import tulipy as ti
import pandas as pd


class Strategy():
    def __init__(self, client, timeframe='5m'):
        self.client = client
        self.timeframe = timeframe

    def predict(self):
        ohlcv_candles = pd.DataFrame(self.client.Trade.Trade_getBucketed(
            binSize=self.timeframe,
            symbol='XBTUSD',
            count=50,
            reverse=True
        ).result()[0])

        ohlcv_candles.set_index(['timestamp'], inplace=True)
        import pdb; pdb.set_trace()

        # hist = ti.cci(ohlcv_candles.high.values, ohlcv_candles.low.values, ohlcv_candles.close.values, 10)
        hist = talib.CCI(ohlcv_candles['high'], ohlcv_candles['low'], ohlcv_candles.close.values, 10)

        # sell
        if hist[-1] < 0:
            return -1
        # buy
        elif hist[-1] > 0:
            return 1
        # do nothing
        else:
            return macd[0]