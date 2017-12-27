import time
from pprint import pprint
from exchange import Exchange
from statistics import PeriodRange
from statistics import Statistics

class AssetVsBtc:

    def __init__(self, assetName):
        self.assetName = assetName
        self.exchange = Exchange()
        self.statistics = Statistics()
        self.previousPrice = 0
        self.buyPrice = 0
        self.assetBought = False

    def asset_vs_btc(self):
        result = self.statistics.get_asset(self.assetName)
        currentPrice = result[0]["price_btc"]

        if (self.previousPrice == 0):
            self.previousPrice = currentPrice

        print("          current       price: %s" %currentPrice)
        print("          previousPrice price: %s" %self.previousPrice)

        if (float(currentPrice) > float(self.previousPrice)):
            if(self.assetBought == False):
                self.buyPrice = currentPrice
                print("Buy %s at %s" %(self.assetName, self.buyPrice))
                self.assetBought = True
        else:
            if(self.assetBought == True):
                percentage = (float(currentPrice) - float(self.buyPrice)) / float(self.buyPrice) * 100
                print("Sell %s at %s with percentage %s" %(self.assetName, currentPrice, percentage))
                self.assetBought = False

        self.previousPrice = currentPrice

    def run(self):
        print("Strategy %s vs BTC" %self.assetName)
        while True:
            self.asset_vs_btc()
            time.sleep(900) # Sleep 15 minutes
