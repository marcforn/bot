import time
from pprint import pprint
from exchange import Exchange
from statistics import PeriodRange
from statistics import Statistics

class BestAsset:

    def __init__(self, period, limit):
        self.period = period
        self.limit = limit
        self.exchange = Exchange()
        self.statistics = Statistics()
        self.currentAssetId = None

        self.buyPrice = 0

    def best_asset(self):
        bestAssetId = self.statistics.get_best_asset(self.period, self.limit)
        if (bestAssetId != self.currentAssetId):
            # Sell current asset
            self.exchange.sell_asset(self.currentAssetId)

            if (self.currentAssetId != None):
                asset = self.statistics.get_asset(self.currentAssetId)
                currentPrice = asset[0]["price_eur"]
                percentage = (float(currentPrice) - float(self.buyPrice)) / float(self.buyPrice) * 100
                print("Selling asset %s at %s with percentage %s" %(self.currentAssetId, currentPrice, percentage))

            # Buy best asset
            self.exchange.buy_asset(bestAssetId)

            if (bestAssetId != None):
                asset = self.statistics.get_asset(bestAssetId)
                self.buyPrice = asset[0]["price_eur"]
                print("Buying asset %s at %s" %(bestAssetId, self.buyPrice))

            # Set new current asset
            self.currentAssetId = bestAssetId

    def run(self):
        print("Strategy Best Asset %s of %s" %(self.period.value, self.limit))
        while True:
            self.best_asset()
            time.sleep(10) # Sleep 10 seconds
