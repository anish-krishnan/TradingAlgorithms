"""
This class implements a standard Portfolio API.
"""


class Portfolio(object):
    def __init__(self, balance=25000):
        self.initial_balance = balance

        # Mapping symbols to quantity of stocks
        self.portfolio = dict()

        # Mapping symbols to average price per share
        self.investment_prices = dict()

        self.balance = balance

        self.debug = True

    def can_buy(self, sym, price, quantity):
        return price * quantity <= self.balance

    def can_sell(self, sym, price, quantity):
        return (sym in self.portfolio) and (quantity <= self.portfolio[sym])

    def buy(self, sym, price, quantity):
        if not self.can_buy(sym, price, quantity):
            raise "Not enough money to buy stock"

        if sym not in self.portfolio:
            self.portfolio[sym] = quantity
            self.investment_prices[sym] = price
        else:
            cur_quantity = self.portfolio[sym]
            cur_price_per_share = self.investment_prices[sym]
            self.portfolio[sym] += quantity

            total_investment_value = (cur_quantity * cur_price_per_share) + (
                quantity * price
            )
            price_per_share = total_investment_value / (cur_quantity + quantity)
            self.investment_prices[sym] = price_per_share

        self.balance -= price * quantity

    def sell(self, sym, price, quantity):
        if not self.can_sell(sym, price, quantity):
            raise "Not enough stocks to sell"
        self.portfolio[sym] -= quantity
        self.balance += price * quantity

    def get_quantity(self, sym):
        if sym not in self.portfolio:
            return 0
        return self.portfolio[sym]

    def get_balance(self):
        return self.balance

    def get_holding_cash(self, price_map):
        totalMoney = 0
        for sym in self.portfolio:
            totalMoney += self.portfolio[sym] * price_map[sym]
        return totalMoney

    def get_total_net_worth(self, price_map):
        totalMoney = self.balance + self.get_holding_cash(price_map)
        return ((totalMoney / self.initial_balance) - 1) * 100

    def get_total_net_worth_cash(self, price_map):
        totalMoney = self.balance + self.get_holding_cash(price_map)
        return totalMoney - self.initial_balance

    def profit_and_loss(self, price_map):
        holding_cash = self.get_holding_cash(price_map)
        total_spent = 0
        for sym in self.portfolio:
            total_spent += self.portfolio[sym] * self.investment_prices[sym]
        return ((holding_cash / total_spent) - 1) * 100

    def print_d(*args):
        if self.debug:
            print(*args)
