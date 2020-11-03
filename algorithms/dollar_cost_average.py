"""
This class implements the Algorithm abstract class.

We define the dollar cost averaging algorithm.
The algorithm is implemented based on: 
https://www.investopedia.com/terms/d/dollarcostaveraging.asp#:~:text=Dollar%2Dcost%20averaging%20(DCA)%20is%20an%20investment%20strategy%20in,volatility%20on%20the%20overall%20purchase.&text=Dollar%2Dcost%20averaging%20is%20also%20known%20as%20the%20constant%20dollar%20plan.
"""

from algorithms.algorithm import Algorithm

from datetime import datetime


class DollarCostAverage(Algorithm):
    def __init__(self):
        super().__init__()
        self.covered_months = set()

    def trade(self, sym, data):
        today_price = data.iloc[0].close
        today_date = datetime.strptime(data.index[0], "%Y-%m-%d")
        month_year = today_date.strftime("%Y-%m")

        if month_year in self.covered_months:
            # we have already invested this month
            return
        self.covered_months.add(month_year)

        amount_to_invest = 100

        num_shares = amount_to_invest / today_price
        if self.portfolio.can_buy(sym, today_price, num_shares):
            self.portfolio.buy(sym, today_price, num_shares)
