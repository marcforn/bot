import time
import csv
from pprint import pprint
from exchange import Exchange
from statistics import PeriodRange
from statistics import Statistics

class BestAsset:

    def __init__(self, period, limit):
        self.period = period
        self.limit = limit
        self.exchange = Exchange()
        self.statistics = Statistics(default="USDT")
        self.currentAssetSymbol = None

        self.buyPrice = 0

    def best_asset(self):
        try:
            bestAssetSymbol = self.statistics.get_best_asset(self.period, self.limit)
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
        print("Strategy Best Asset %s of %d" %(self.period.value, self.limit))
        while True:
            self.best_asset()
            time.sleep(10) # Sleep 10 seconds
