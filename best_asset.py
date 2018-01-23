import time
import csv
from pprint import pprint
from exchange import Exchange
from statistics import PeriodRange
from statistics import Statistics

class BestAsset:

    def __init__(self, period):
        self.period = period
        self.statistics = Statistics(default="USDT")
        self.exchange = Exchange(default="USDT")
        self.currentAssetSymbol = None

    def best_asset(self):
        try:
            tickerRange = ["BTC", "ETH", "NEO", "BNB", "LTC", "BCH"]
            bestAssetSymbol = self.statistics.get_best_asset(self.period, tickerRange)
            if (bestAssetSymbol != self.currentAssetSymbol):
                # Print on console best asset
                print("Best Asset: %s" %(bestAssetSymbol))

                # Sell all assets
                self.exchange.sell_all_assets()

                # Buy best asset
                self.exchange.buy_asset(bestAssetSymbol)

                # Set new current asset
                self.currentAssetSymbol = bestAssetSymbol
        except Exception as e:
            print(e)
            pass

    def run(self):
        print("Strategy Best Asset %s" %(self.period.value))
        while True:
            self.best_asset()
            time.sleep(10) # Sleep 10 seconds
