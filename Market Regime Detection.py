class MarketRegime:

    def detect(self, atr, adx):

        if adx > 25:
            return "TREND"

        return "RANGE"
