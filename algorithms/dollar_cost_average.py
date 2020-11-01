"""
This class implements the Algorithm abstract class.

We define a basic trading algorithm. We buy a stock if
its price today is lower than its price yesterday.
"""

from algorithms.algorithm import Algorithm
from datetime import datetime


class DollarCostAverage(Algorithm):
    def __init__(self):
        super().__init__()
        self.covered_months = {}

    def trade(self, sym, data):
        today_date = datetime.strptime(data.index[0], "%Y-%m-%d")
        month_year = today_date.strftime("%Y-%m")

        if month_year in self.covered_months:
            # we have already invested this month
            return

        amount_to_invest = 100
        today_price = data.iloc[0].close

        num_shares = amount_to_invest / today_price
        if self.portfolio.can_buy(sym, today_price, num_shares):
            self.portfolio.buy(sym, today_price, num_shares)
