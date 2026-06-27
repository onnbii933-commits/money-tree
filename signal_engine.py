import pandas as pd

class SignalEngine:

    def signal(self, df):

        ema20 = (
            df["close"]
            .ewm(span=20)
            .mean()
        )

        ema50 = (
            df["close"]
            .ewm(span=50)
            .mean()
        )

        if ema20.iloc[-1] > ema50.iloc[-1]:
            return "BUY"

        if ema20.iloc[-1] < ema50.iloc[-1]:
            return "SELL"

        return "HOLD"
