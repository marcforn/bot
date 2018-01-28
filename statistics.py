import enum
from coinmarketcap import Market


class PeriodRange(enum.Enum):
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"


class Statistics:

    def __init__(self, default):
        self.market = Market()
        self.default = default

    def get_best_asset(self, period, ticker_range):
        best_asset_symbol = self.default
        best_asset_percentage = 0

        response = self.market.ticker(limit=100, convert='USD')
        ticker_list_length = len(response)
        for i in range(0, ticker_list_length):
            item = response[i]

            if item["symbol"] in str(ticker_range):
                if period == PeriodRange.HOUR:
                    if float(item["percent_change_1h"]) > float(best_asset_percentage):
                        best_asset_symbol = item["symbol"]
                        best_asset_percentage = item["percent_change_1h"]
                elif period == PeriodRange.DAY:
                    if float(item["percent_change_24h"]) > float(best_asset_percentage):
                        best_asset_symbol = item["symbol"]
                        best_asset_percentage = item["percent_change_24h"]
                elif period == PeriodRange.WEEK:
                    if float(item["percent_change_7d"]) > float(best_asset_percentage):
                        best_asset_symbol = item["symbol"]
                        best_asset_percentage = item["percent_change_7d"]

        return best_asset_symbol
