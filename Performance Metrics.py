class Metrics:

    def profit_factor(
        self,
        gross_profit,
        gross_loss
    ):

        if gross_loss == 0:
            return 0

        return gross_profit / gross_loss
