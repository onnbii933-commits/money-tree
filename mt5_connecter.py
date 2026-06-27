import MetaTrader5 as mt5

class MT5Connector:

    def connect(self):

        if not mt5.initialize():
            raise Exception(
                "MT5 initialization failed"
            )

        return True

    def account_info(self):

        info = mt5.account_info()

        return info

    def symbol_price(self, symbol):

        tick = mt5.symbol_info_tick(
            symbol
        )

        return {
            "bid": tick.bid,
            "ask": tick.ask
        }
