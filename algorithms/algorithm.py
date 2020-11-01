"""
This class lays out the interface for a trading algorithm.

The algorithm will hold on to a portfolio that it uses to
determine the global state and execute trades. 

We also define the trade method which is called on a recurring
basis. The algorithm will use new data to make decisions 
around new trades.
"""
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from portfolio import Portfolio


class Algorithm(object):
    def __init__(self):
        self.portfolio = Portfolio()

    # The trade method is called with new data on a daily basis.
    # The algorithm will make decisions around new trades with
    # this "new" information
    def trade(self, sym, data):
        pass