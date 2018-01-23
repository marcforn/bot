import enum
from coinmarketcap import Market
from pprint import pprint

class PeriodRange(enum.Enum):
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"

class Statistics:

    def __init__(self, default):
      self.market = Market()
      self.default = default

    def get_asset(self, assetName):
        asset = self.market.ticker(currency=assetName, convert='EUR')
        return asset

    def get_best_asset(self, period, limit):
        bestAssetSymbol = self.default
        bestAssetPercentage = 0

        response = self.market.ticker(limit=limit, convert='EUR')
        tickerListLenght = len(response)
        for i in range(0, tickerListLenght):
            item = response[i]

            if (period == PeriodRange.HOUR):
                if (float(item["percent_change_1h"]) > float(bestAssetPercentage)):
                    bestAssetSymbol = item["symbol"]
                    bestAssetPercentage = item["percent_change_1h"]
            elif (period == PeriodRange.DAY):
                if (float(item["percent_change_24h"]) > float(bestAssetPercentage)):
                    bestAssetSymbol = item["symbol"]
                    bestAssetPercentage = item["percent_change_24h"]
            elif (period == PeriodRange.WEEK):
                if (float(item["percent_change_7d"]) > float(bestAssetPercentage)):
                    bestAssetSymbol = item["symbol"]
                    bestAssetPercentage = item["percent_change_7d"]

        return bestAssetSymbol
