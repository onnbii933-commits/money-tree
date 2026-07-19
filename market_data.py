import MetaTrader5 as mt5

class MarketData:

    def get_tick(self, symbol):

        tick = mt5.symbol_info_tick(
            symbol
        )

        return {
            "bid": tick.bid,
            "ask": tick.ask
        }
