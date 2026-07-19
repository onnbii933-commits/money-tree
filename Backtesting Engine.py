class BacktestEngine:

    def run(
        self,
        strategy,
        historical_data
    ):

        trades = strategy.execute(
            historical_data
        )

        return trades
