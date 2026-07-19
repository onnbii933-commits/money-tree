import pandas as pd

class FeatureEngineering:

    def build(self, df):

        df["ema20"] = df.close.ewm(span=20).mean()
        df["ema50"] = df.close.ewm(span=50).mean()

        df["returns"] = df.close.pct_change()

        return df.dropna()
