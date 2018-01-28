import time
from exchange import Exchange
from statistics import Statistics


class BestAsset:

    def __init__(self, period):
        self.period = period
        self.statistics = Statistics(default="USDT")
        self.exchange = Exchange(default="USDT")
        self.currentAssetSymbol = None

    def best_asset(self):
        try:
            ticker_range = ["BTC", "ETH", "NEO", "BNB", "LTC", "BCH"]
            best_asset_symbol = self.statistics.get_best_asset(self.period, ticker_range)
            if best_asset_symbol != self.currentAssetSymbol:
                # Print on console best asset
                print("Best Asset: %s" % best_asset_symbol)

                # Sell all assets
                self.exchange.sell_all_assets()

                # Buy best asset
                self.exchange.buy_asset(best_asset_symbol)

                # Set new current asset
                self.currentAssetSymbol = best_asset_symbol
        except Exception as e:
            print(e)
            pass

    def run(self):
        print("Strategy Best Asset %s" % self.period.value)
        while True:
            self.best_asset()
            time.sleep(10)  # Sleep 10 seconds
