"""
This script allows us to download financial data on 
varying granularity levels
"""


from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time

API_KEY = open("credentials/apikey1.txt", "r").read()


def downloadData(symbol, timeInterval):
    ts = TimeSeries(key=API_KEY, output_format="pandas")
    ti = TechIndicators(key=API_KEY, output_format="pandas")

    stock_data = None

    # Case on timeInterval to get correct data
    if timeInterval == "daily":
        stock_data, _ = ts.get_daily(symbol=symbol, outputsize="full")
    elif timeInterval == "weekly":
        stock_data, _ = ts.get_weekly(symbol=symbol)
    elif timeInterval == "monthly":
        stock_data, _ = ts.get_monthly(symbol=symbol)
    elif timeInterval in ["1min", "5min", "15min", "30min", "60min"]:
        stock_data, _ = ts.get_intraday(
            symbol=symbol, interval=timeInterval, outputsize="full"
        )
    else:
        raise "Invalid timeInterval"

    waitTime = 15

    print("stock", stock_data)
    stock_data.to_csv("data/" + timeInterval + "/" + symbol + "_stock.csv")
    time.sleep(waitTime)

    # rsi_data, _ = ti.get_rsi(symbol=symbol, interval=timeInterval, time_period=14, series_type='close')
    # print("rsi", rsi_data)
    # rsi_data.to_csv("data/"+timeInterval+"/"+symbol+"_rsi_14.csv")
    # time.sleep(waitTime)

    # adx_data, _ = ti.get_adx(symbol=symbol, interval=timeInterval, time_period=14)
    # print("adx", adx_data)
    # adx_data.to_csv("data/"+timeInterval+"/"+symbol+"_adx_14.csv")
    # time.sleep(waitTime)

    # dx_data, _ = ti.get_dx(symbol=symbol, interval=timeInterval, time_period=200)
    # print("dx", dx_data)
    # dx_data.to_csv("data/"+timeInterval+"/"+symbol+"_dx_14.csv")
    # time.sleep(waitTime)

    # cci_data, _ = ti.get_cci(symbol=symbol, interval=timeInterval, time_period=14)
    # print("cci", cci_data)
    # cci_data.to_csv("data/"+timeInterval+"/"+symbol+"_cci_14.csv")
    # time.sleep(waitTime)

    # ad_data, _ = ti.get_ad(symbol=symbol, interval=timeInterval)
    # print("ad", ad_data)
    # ad_data.to_csv("data/"+timeInterval+"/"+symbol+"_ad.csv")
    # time.sleep(waitTime)

    # sma50_data, _ = ti.get_sma(symbol=symbol, interval=timeInterval, time_period=50)
    # print("sma50", sma50_data)
    # sma50_data.to_csv("data/"+timeInterval+"/"+symbol+"_sma50.csv")
    # time.sleep(waitTime)

    # sma200_data, _ = ti.get_sma(symbol=symbol, interval=timeInterval, time_period=200)
    # print("sma200", sma200_data)
    # sma200_data.to_csv("data/"+timeInterval+"/"+symbol+"_sma200.csv")
    # time.sleep(waitTime)

    # sma5_data, _ = ti.get_sma(symbol=symbol, interval=timeInterval, time_period=5)
    # print("sma5", sma5_data)
    # sma5_data.to_csv("data/"+timeInterval+"/"+symbol+"_sma5.csv")
    # time.sleep(waitTime)

    # sma20_data, _ = ti.get_sma(symbol=symbol, interval=timeInterval, time_period=20)
    # print("sma20", sma20_data)
    # sma20_data.to_csv("data/"+timeInterval+"/"+symbol+"_sma20.csv")
    # time.sleep(waitTime)

    # sma10_data, _ = ti.get_sma(symbol=symbol, interval=timeInterval, time_period=10)
    # print("sma10", sma10_data)
    # sma10_data.to_csv("data/"+timeInterval+"/"+symbol+"_sma10.csv")
    # time.sleep(waitTime)


if __name__ == "__main__":
    stocks = ["JPM", "DAL", "SPY"]
    for stock in stocks:
        downloadData(stock, "daily")