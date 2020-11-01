"""
This algorithm is an EXAMPLE to showcase an implementation
of the Algorithm abstract class.

We define a basic trading algorithm. We buy a stock if
its price today is higher than its price yesterday.
"""

from algorithms.algorithm import Algorithm


class BasicAlgo(Algorithm):
    def __init__(self):
        super().__init__()

    def trade(self, sym, data):

        today_price = data.iloc[0].close
        yest_price = data.iloc[1].close

        quantity = 1

        if today_price > yest_price and self.portfolio.can_buy(
            sym, today_price, quantity
        ):
            self.portfolio.buy(sym, today_price, quantity)
        elif today_price < yest_price and self.portfolio.can_sell(
            sym, today_price, quantity
        ):
            self.portfolio.sell(sym, today_price, quantity)
