class RiskManager:

    MAX_DAILY_LOSS = 5
    MAX_LOT_SIZE = 1.0

    def validate_trade(
        self,
        drawdown,
        lot_size
    ):

        if drawdown >= self.MAX_DAILY_LOSS:
            return False

        if lot_size > self.MAX_LOT_SIZE:
            return False

        return True
