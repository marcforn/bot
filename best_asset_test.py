import time
import csv
from exchange import Exchange
from statistics import Statistics


class BestAssetTest:

    def __init__(self, period):
        self.period = period
        self.statistics = Statistics(default="USDT")
        self.exchange = Exchange(default="USDT")
        self.current_asset_symbol = None

        self.buyPrice = 0

    def best_asset(self):
        try:
            ticker_range = ["BTC", "ETH", "NEO", "BNB", "LTC", "BCH"]
            best_asset_symbol = self.statistics.get_best_asset(self.period, ticker_range)

            if best_asset_symbol != self.current_asset_symbol:
                if self.current_asset_symbol is not None:
                    current_price = self.exchange.get_asset_price(self.current_asset_symbol)

                    print(current_price)
                    percentage = (float(current_price) - float(self.buyPrice)) / float(self.buyPrice) * 100
                    print("Selling asset %s at %s with percentage %s" % (
                        self.current_asset_symbol, current_price, percentage))

                    file_name = "output_%s.csv" % self.period.value
                    file = open(file_name, 'a')
                    try:
                        writer = csv.writer(file)
                        writer.writerow((self.current_asset_symbol, self.buyPrice, current_price, percentage))
                    finally:
                        file.close()

                if best_asset_symbol is not None:
                    self.buyPrice = self.exchange.get_asset_price(best_asset_symbol)
                    print("Buying asset %s at %s" % (best_asset_symbol, self.buyPrice))

                # Set new current asset
                self.current_asset_symbol = best_asset_symbol
        except Exception as e:
            print(e)
            pass

    def run(self):
        print("[TEST] Strategy Best Asset %s" % self.period.value)
        while True:
            self.best_asset()
            time.sleep(10)  # Sleep 10 seconds
