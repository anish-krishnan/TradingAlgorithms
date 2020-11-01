"""
This is a backtesting framework to test various trading
strategies.
"""

from algorithms.basic_algo import BasicAlgo
from algorithms.dollar_cost_average import DollarCostAverage
import pandas as pd
import numpy as np
from tabulate import tabulate


HISTORY_LENGTH = 5
OUTPUT = """
Trading Period: {} - {}

{}
"""


def get_stats(algo, symbol, stock_data):
    start_date = stock_data.index[HISTORY_LENGTH]
    end_date = stock_data.index[-1]
    end_price = stock_data.iloc[-1].close

    holding_cash = np.around(algo.portfolio.get_holding_cash({symbol: end_price}), 2)
    net_worth = np.around(algo.portfolio.get_total_net_worth({symbol: end_price}), 2)
    net_worth_cash = np.around(
        algo.portfolio.get_total_net_worth_cash({symbol: end_price}), 2
    )

    table = [
        ["Holding Cash", holding_cash],
        ["P&L %", net_worth],
        ["P&L $", net_worth_cash],
    ]
    formatted_table = tabulate(table, headers=["Statistics", ""], tablefmt="orgtbl")
    formatted_output = OUTPUT.format(start_date, end_date, formatted_table)
    return formatted_output


def backtest(algo, symbol, timeInterval):

    # Retrieve stock data
    raw_stock_data = pd.read_csv(
        "data/" + timeInterval + "/" + symbol + "_stock.csv", index_col="date"
    )

    stock_data = raw_stock_data.sort_index()

    for i in range(len(stock_data) - HISTORY_LENGTH):
        subset = stock_data[i : i + HISTORY_LENGTH][::-1]
        algo.trade(symbol, subset)

    stats = get_stats(algo, symbol, stock_data)
    print(stats)


if __name__ == "__main__":
    print("\n")

    basicAlgo = BasicAlgo()
    dollarCostAverage = DollarCostAverage()
    # backtest(basicAlgo, "SPY", "daily")
    backtest(dollarCostAverage, "SPY", "daily")

    print("\n")
