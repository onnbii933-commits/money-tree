class DrawdownGuard:

    def allow_trade(
        self,
        current_drawdown,
        max_drawdown
    ):

        return current_drawdown < max_drawdown
