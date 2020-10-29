"""
This class implements a standard Portfolio API.
"""


class Portfolio(object):
    def __init__(self, balance=25000):
        self.initialBalance = balance
        self.portfolio = dict()
        self.balance = balance

        self.debug = 1

    def buy(self, sym, price, quantity):
        if price * quantity > self.balance:
            raise "Not enough money to buy stock"
        if sym not in self.portfolio:
            self.portfolio[sym] = quantity
        else:
            self.portfolio[sym] += quantity
        self.balance -= price * quantity

    def sell(self, sym, price, quantity):
        if sym not in self.portfolio or self.portfolio[sym] < quantity:
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
        return ((totalMoney / self.initialBalance) - 1) * 100

    def get_total_net_worth_cash(self, price_map):
        totalMoney = self.balance + self.get_holding_cash(price_map)
        return totalMoney - self.initialBalance

    def print_d(*args):
        if self.debug:
            print(*args)
