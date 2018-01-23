import time
import csv
from pprint import pprint
from exchange import Exchange
from statistics import PeriodRange
from statistics import Statistics

class BestAssetTest:

    def __init__(self, period):
        self.period = period
        self.statistics = Statistics(default="USDT")
        self.exchange = Exchange(default="USDT")
        self.currentAssetSymbol = None

        self.buyPrice = 0

    def best_asset(self):
        try:
            tickerRange = ["BTC", "ETH", "NEO", "BNB", "LTC", "BCH"]
            bestAssetSymbol = self.statistics.get_best_asset(self.period, tickerRange)

            if (bestAssetSymbol != self.currentAssetSymbol):
                if (self.currentAssetSymbol != None):
                    currentPrice = self.exchange.get_asset_price(self.currentAssetSymbol)

                    print(currentPrice)
                    percentage = (float(currentPrice) - float(self.buyPrice)) / float(self.buyPrice) * 100
                    print("Selling asset %s at %s with percentage %s" %(self.currentAssetSymbol, currentPrice, percentage))

                    fileName = "output_%s.csv" %(self.period.value)
                    file = open(fileName, 'a')
                    try:
                        writer = csv.writer(file)
                        writer.writerow((self.currentAssetSymbol, self.buyPrice, currentPrice, percentage))
                    finally:
                        file.close()

                if (bestAssetSymbol != None):
                    self.buyPrice = self.exchange.get_asset_price(bestAssetSymbol)
                    print("Buying asset %s at %s" %(bestAssetSymbol, self.buyPrice))

                # Set new current asset
                self.currentAssetSymbol = bestAssetSymbol
        except Exception as e:
            print(e)
            pass

    def run(self):
        print("[TEST] Strategy Best Asset %s" %(self.period.value))
        while True:
            self.best_asset()
            time.sleep(10) # Sleep 10 seconds
