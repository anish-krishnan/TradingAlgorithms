"""
This is a backtesting framework to test various trading
strategies.
"""

from algorithms.basic_algo import BasicAlgo
from algorithms.dollar_cost_average import DollarCostAverage

from datetime import datetime
from tabulate import tabulate

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


HISTORY_LENGTH = 5
OUTPUT = """
Trading Period: {} - {}

{}
"""


def get_stats(algo, symbol, stock_data):
    start_date = stock_data.index[HISTORY_LENGTH]
    end_date = stock_data.index[-1]
    end_price = stock_data.iloc[-1].close

    initial_balance = np.around(algo.portfolio.initial_balance, 2)
    balance = np.around(algo.portfolio.get_balance(), 2)
    holding_cash = np.around(algo.portfolio.get_holding_cash({symbol: end_price}), 2)
    net_worth = np.around(algo.portfolio.get_total_net_worth({symbol: end_price}), 2)
    net_worth_cash = np.around(
        algo.portfolio.get_total_net_worth_cash({symbol: end_price}), 2
    )
    profit_and_loss = np.around(algo.portfolio.profit_and_loss({symbol: end_price}), 2)

    table = [
        ["Initial Balance", initial_balance],
        ["Current Balance", balance],
        ["Holding Cash", holding_cash],
        ["Net Worth %", net_worth],
        ["Net Worth $", net_worth_cash],
        ["P&L %", profit_and_loss],
    ]
    formatted_table = tabulate(table, headers=["Statistics", ""], tablefmt="orgtbl")
    formatted_output = OUTPUT.format(start_date, end_date, formatted_table)
    return formatted_output


def plot(symbol, x_plot, **kwargs):
    for name, points in kwargs.items():
        plt.plot(x_plot, points, label=name)
    plt.legend()
    plt.title("Stats for " + symbol)
    plt.show()


def backtest(algo, symbol, start_date, end_date):
    # Retrieve stock data
    stock_data = pd.read_csv(
        "data/daily/" + symbol + "_stock.csv", index_col="date"
    ).sort_index()[start_date:end_date]

    x_plot, stock_plot, investment_plot = [], [], []

    # Call the algorithm's trade function on each day
    # We provide today's price along with historical prices
    for i in range(len(stock_data) - HISTORY_LENGTH):
        subset = stock_data[i : i + HISTORY_LENGTH][::-1]
        algo.trade(symbol, subset)

        x_plot.append(datetime.strptime(stock_data.index[i], "%Y-%m-%d"))
        stock_plot.append(stock_data.iloc[i].close)
        investment_plot.append(algo.portfolio.investment_prices[symbol])

    stats = get_stats(algo, symbol, stock_data)
    print(stats)

    plot(symbol, x_plot, stock=stock_plot, investment=investment_plot)


if __name__ == "__main__":
    print("\n")

    symbol, start_date, end_date = sys.argv[1], sys.argv[2], sys.argv[3]

    basicAlgo = BasicAlgo()
    dollarCostAverage = DollarCostAverage()
    backtest(dollarCostAverage, symbol, start_date, end_date)

    print("\n")
