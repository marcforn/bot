import math
from binance.client import Client
from credentials import *


class Exchange:

    def __init__(self, default):
        self.client = Client(binance_api_key, binance_api_secret)
        self.storage_ticker = default

    def get_asset_price(self, asset_name):
        if asset_name != "USDT":
            ticker = self.client.get_ticker(symbol=asset_name + self.storage_ticker)
            return ticker["lastPrice"]
        else:
            return 1

    def buy_asset(self, asset_name):
        if asset_name != self.storage_ticker:
            # Print on console buy order
            print("Buying asset: %s" % asset_name)

            # Set asset name according mapper CoinMarketCap vs Binance
            asset_name = self.mapper_asset_name(asset_name)

            # Get free balance to trade
            result = self.client.get_asset_balance(asset=self.storage_ticker)
            free_balance = result["free"]

            # Get price asset vs storage ticker
            result = self.client.get_symbol_ticker(symbol=asset_name + self.storage_ticker)
            price = result["price"]

            # Max quantity to buy
            quantity = (float(free_balance) / float(price))

            factor = 1 * math.pow(10, self.mapper_min_quantity(asset_name))
            quantity = math.floor(quantity * factor) / factor
            print("quantity round %s" % quantity)

            # Submit a buy order
            self.client.order_market_buy(symbol=asset_name + self.storage_ticker, quantity=quantity)

    def sell_all_assets(self):
        response = self.client.get_account()
        balance_lenght = len(response["balances"])
        for i in range(0, balance_lenght):
            item = response["balances"][i]
            if item["asset"] != self.storage_ticker and float(item["free"]) > 0:
                try:
                    factor = 1 * math.pow(10, self.mapper_min_quantity(item["asset"]))
                    quantity = math.floor(float(item["free"]) * factor) / factor

                    if quantity > 0:
                        # Print on console buy order
                        print("Selling asset: %s" % (item["asset"]))
                        self.client.order_market_sell(symbol=item["asset"] + self.storage_ticker, quantity=quantity)
                except Exception as e:
                    print(e)
                    pass

    def mapper_asset_name(self, asset_name):
        if asset_name == "USDT":
            return "USDT"
        elif asset_name == "BTC":
            return "BTC"
        elif asset_name == "ETH":
            return "ETH"
        elif asset_name == "XRP":
            return "XRP"
        elif asset_name == "BCH":
            return "BCC"
        elif asset_name == "ADA":
            return "ADA"
        elif asset_name == "LTC":
            return "LTC"
        elif asset_name == "XEM":
            return "XEM"
        elif asset_name == "NEO":
            return "NEO"
        elif asset_name == "XLM":
            return "XLM"
        elif asset_name == "MIOTA":
            return "IOTA"
        elif asset_name == "BNB":
            return "BNB"

    def mapper_min_quantity(self, asset_name):
        if asset_name == "USDT":
            return 4
        elif asset_name == "BTC":
            return 6
        elif asset_name == "ETH":
            return 5
        elif asset_name == "XRP":
            return 0
        elif asset_name == "BCC":
            return 5
        elif asset_name == "ADA":
            return 0
        elif asset_name == "LTC":
            return 5
        elif asset_name == "XEM":
            return 0
        elif asset_name == "NEO":
            return 3
        elif asset_name == "XLM":
            return 1
        elif asset_name == "IOTA":
            return 0
        elif asset_name == "BNB":
            return 2
