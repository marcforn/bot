import math
import json
from binance.client import Client
from binance.enums import *
from credentials import *
from pprint import pprint


class Exchange:

    def __init__(self, default):
      self.client = Client(binance_api_key, binance_api_secret)
      self.storageTicker = default

    def get_asset_price(self, assetName):
        if (assetName != "USDT"):
            ticker = self.client.get_ticker(symbol=assetName + self.storageTicker)
            return ticker["lastPrice"]
        else:
            return 1

    def buy_asset(self, assetName):
        if (assetName != self.storageTicker):
            # Print on console buy order
            print("Buying asset: %s" %(assetName))

            # Set asset name according mapper CoinMarketCap vs Binance
            assetName = self.mapper_assetName(assetName)

            # Get free balance to trade
            result = self.client.get_asset_balance(asset=self.storageTicker)
            freebalance = result["free"]

            # Get price asset vs storage ticker
            result = self.client.get_symbol_ticker(symbol=assetName + self.storageTicker)
            price = result["price"]

            # Max quantity to buy
            quantity = (float(freebalance) / float(price))

            factor = 1 * math.pow(10, self.mapper_min_quantity(assetName))
            quantity = math.floor(quantity * factor) / factor
            print("quantity round %s" %quantity)

            # Submit a buy order
            order = self.client.order_market_buy(symbol=assetName + self.storageTicker, quantity=quantity)

    def sell_all_assets(self):
        response = self.client.get_account()
        balanceLenght = len(response["balances"])
        for i in range(0, balanceLenght):
            item = response["balances"][i]
            if (item["asset"] != self.storageTicker and float(item["free"]) > 0):
                try:
                    factor = 1 * math.pow(10, self.mapper_min_quantity(item["asset"]))
                    quantity = math.floor(float(item["free"]) * factor) / factor

                    if (quantity > 0):
                        # Print on console buy order
                        print("Selling asset: %s" %(item["asset"]))
                        order = self.client.order_market_sell(symbol=item["asset"] + self.storageTicker, quantity=quantity)
                except Exception as e:
                    print(e)
                    pass

    def mapper_assetName(self, assetName):
        if (assetName == "USDT"):
            return "USDT"
        elif (assetName == "BTC"):
            return "BTC"
        elif (assetName == "ETH"):
            return "ETH"
        elif (assetName == "XRP"):
            return "XRP"
        elif (assetName == "BCH"):
            return "BCC"
        elif (assetName == "ADA"):
            return "ADA"
        elif (assetName == "LTC"):
            return "LTC"
        elif (assetName == "XEM"):
            return "XEM"
        elif (assetName == "NEO"):
            return "NEO"
        elif (assetName == "XLM"):
            return "XLM"
        elif (assetName == "MIOTA"):
            return "IOTA"
        elif (assetName == "BNB"):
            return "BNB"

    def mapper_min_quantity(self, assetName):
        if (assetName == "USDT"):
            return 4
        elif (assetName == "BTC"):
            return 6
        elif (assetName == "ETH"):
            return 5
        elif (assetName == "XRP"):
            return 0
        elif (assetName == "BCC"):
            return 5
        elif (assetName == "ADA"):
            return 0
        elif (assetName == "LTC"):
            return 5
        elif (assetName == "XEM"):
            return 0
        elif (assetName == "NEO"):
            return 3
        elif (assetName == "XLM"):
            return 1
        elif (assetName == "IOTA"):
            return 0
        elif (assetName == "BNB"):
            return 2
