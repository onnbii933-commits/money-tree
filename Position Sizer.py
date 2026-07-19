class PositionSizer:

    def calculate(
        self,
        balance,
        risk_percent,
        stop_loss_pips
    ):

        risk_amount = balance * risk_percent

        return risk_amount / stop_loss_pips
