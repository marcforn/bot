import enum
from coinmarketcap import Market
from pprint import pprint

class PeriodRange(enum.Enum):
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"

class Statistics:

    def __init__(self):
      self.market = Market()

    def get_asset(self, assetName):
        asset = self.market.ticker(currency=assetName, convert='EUR')
        return asset

    def get_best_asset(self, period, limit):
        bestAssetId = "bitcoin"
        bestAssetPercentage = -100

        response = self.market.ticker(limit=limit, convert='EUR')
        tickerListLenght = len(response)
        for i in range(0, tickerListLenght):
            item = response[i]

            if (period == PeriodRange.HOUR):
                if (float(item["percent_change_1h"]) > float(bestAssetPercentage)):
                    bestAssetId = item["id"]
                    bestAssetPercentage = item["percent_change_1h"]
            elif (period == PeriodRange.DAY):
                if (float(item["percent_change_24h"]) > float(bestAssetPercentage)):
                    bestAssetId = item["id"]
                    bestAssetPercentage = item["percent_change_24h"]
            elif (period == PeriodRange.WEEK):
                if (float(item["percent_change_7d"]) > float(bestAssetPercentage)):
                    bestAssetId = item["id"]
                    bestAssetPercentage = item["percent_change_7d"]

        return bestAssetId

    def get_worst_asset(self, period, limit):
        worstAssetId = "bitcoin"
        worstAssetPercentage = 1000

        response = self.market.ticker(limit=limit, convert='EUR')
        tickerListLenght = len(response)
        for i in range(0, tickerListLenght):
            item = response[i]

            if (period == PeriodRange.HOUR):
                if (float(item["percent_change_1h"]) < float(worstAssetPercentage)):
                    worstAssetId = item["id"]
                    worstAssetPercentage = item["percent_change_1h"]
            elif (period == PeriodRange.DAY):
                if (float(item["percent_change_24h"]) < float(worstAssetPercentage)):
                    worstAssetId = item["id"]
                    worstAssetPercentage = item["percent_change_24h"]
            elif (period == PeriodRange.WEEK):
                if (float(item["percent_change_7d"]) > float(worstAssetPercentage)):
                    worstAssetId = item["id"]
                    worstAssetPercentage = item["percent_change_7d"]

        return worstAssetId
