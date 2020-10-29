"""
This file contains a set of unit tests for the
Portfolio module.
"""

from portfolio import Portfolio

import unittest
import numpy as np


class TestPortfolio(unittest.TestCase):

    # Testing buy and sell methods
    def test_buy_and_sell(self):
        portfolio = Portfolio(1000)

        # Buy 2 Apple
        portfolio.buy("AAPL", 50, 2)
        self.assertEqual(portfolio.initialBalance, 1000)
        self.assertEqual(portfolio.get_balance(), 900)
        self.assertEqual(portfolio.portfolio, {"AAPL": 2})

        # Buy 4 Google
        portfolio.buy("GOOG", 100, 4)
        self.assertEqual(portfolio.initialBalance, 1000)
        self.assertEqual(portfolio.get_balance(), 500)
        self.assertEqual(portfolio.portfolio, {"AAPL": 2, "GOOG": 4})

        # Sell 1 Apple
        portfolio.sell("AAPL", 75, 1)
        self.assertEqual(portfolio.initialBalance, 1000)
        self.assertEqual(portfolio.get_balance(), 575)
        self.assertEqual(portfolio.portfolio, {"AAPL": 1, "GOOG": 4})

        # Attempt to sell 2 Apple and buy 10 Apple
        with self.assertRaises(Exception):
            portfolio.sell("AAPL", 75, 2)
        with self.assertRaises(Exception):
            portfolio.buy("AAPL", 100, 10)
        self.assertEqual(portfolio.initialBalance, 1000)
        self.assertEqual(portfolio.get_balance(), 575)
        self.assertEqual(portfolio.portfolio, {"AAPL": 1, "GOOG": 4})

    # Test get_quantity method
    def test_quantity(self):
        portfolio = Portfolio(1000)
        portfolio.buy("AAPL", 50, 2)
        portfolio.buy("GOOG", 100, 4)

        self.assertEqual(portfolio.get_quantity("AAPL"), 2)
        self.assertEqual(portfolio.get_quantity("GOOG"), 4)
        self.assertEqual(portfolio.get_quantity("MSFT"), 0)

    # Test get_holding_cash method
    def test_get_holding_cash(self):
        portfolio = Portfolio(1000)
        portfolio.buy("AAPL", 50, 2)
        portfolio.buy("GOOG", 100, 4)

        price_map = {"AAPL": 100, "GOOG": 150}
        self.assertEqual(portfolio.get_holding_cash(price_map), 800)

    # Test get_total_net_worth method
    def test_get_total_net_worth(self):
        portfolio = Portfolio(1000)
        portfolio.buy("AAPL", 50, 2)
        portfolio.buy("GOOG", 100, 4)

        price_map = {"AAPL": 100, "GOOG": 150}
        np.testing.assert_almost_equal(portfolio.get_total_net_worth(price_map), 30)

    # Test get_total_net_worth_cash method
    def test_get_total_net_worth_cash(self):
        portfolio = Portfolio(1000)
        portfolio.buy("AAPL", 50, 2)
        portfolio.buy("GOOG", 100, 4)

        price_map = {"AAPL": 100, "GOOG": 150}
        np.testing.assert_almost_equal(
            portfolio.get_total_net_worth_cash(price_map), 300
        )


if __name__ == "__main__":
    unittest.main()