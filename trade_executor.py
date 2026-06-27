import MetaTrader5 as mt5

class TradeExecutor:

    def buy(self, symbol, lot):

        tick = mt5.symbol_info_tick(
            symbol
        )

        request = {

            "action":
            mt5.TRADE_ACTION_DEAL,

            "symbol":
            symbol,

            "volume":
            lot,

            "type":
            mt5.ORDER_TYPE_BUY,

            "price":
            tick.ask,

            "deviation":
            20,

            "magic":
            10001,

            "comment":
            "AI BUY"
        }

        return mt5.order_send(
            request
        )

    def sell(self, symbol, lot):

        tick = mt5.symbol_info_tick(
            symbol
        )

        request = {

            "action":
            mt5.TRADE_ACTION_DEAL,

            "symbol":
            symbol,

            "volume":
            lot,

            "type":
            mt5.ORDER_TYPE_SELL,

            "price":
            tick.bid,

            "deviation":
            20,

            "magic":
            10001,

            "comment":
            "AI SELL"
        }

        return mt5.order_send(
            request
        )
