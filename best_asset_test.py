import time
import csv
from pprint import pprint
from exchange import Exchange
from statistics import PeriodRange
from statistics import Statistics

class BestAssetTest:

    def __init__(self, period, limit):
        self.period = period
        self.limit = limit
        self.exchange = Exchange()
        self.statistics = Statistics(default="USDT")
        self.currentAssetId = None

        self.buyPrice = 0

    def best_asset(self):
        try:
            bestAssetId = self.statistics.get_best_asset(self.period, self.limit)
            if (bestAssetId != self.currentAssetId):

                if (self.currentAssetId != None):
                    asset = self.statistics.get_asset(self.currentAssetId)
                    currentPrice = asset[0]["price_eur"]
                    percentage = (float(currentPrice) - float(self.buyPrice)) / float(self.buyPrice) * 100
                    print("Selling asset %s at %s with percentage %s" %(self.currentAssetId, currentPrice, percentage))

                    fileName = "output_%s_%d.csv" %(self.period.value, self.limit)
                    file = open(fileName, 'a')
                    try:
                        writer = csv.writer(file)
                        writer.writerow((self.currentAssetId, self.buyPrice, currentPrice, percentage))
                    finally:
                        file.close()

                if (bestAssetId != None):
                    asset = self.statistics.get_asset(bestAssetId)
                    self.buyPrice = asset[0]["price_eur"]
                    print("Buying asset %s at %s" %(bestAssetId, self.buyPrice))

                # Set new current asset
                self.currentAssetId = bestAssetId
        except Exception as e:
            print(e)
            pass

    def run(self):
        print("[TEST] Strategy Best Asset %s of %d" %(self.period.value, self.limit))
        while True:
            self.best_asset()
            time.sleep(10) # Sleep 10 seconds
