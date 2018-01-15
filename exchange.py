import json
from binance.client import Client
from binance.enums import *
from pprint import pprint

api_key="Jzw15ulU3mXONnEDsUHShwGY6tJC4MfdJorsUn5KC01yaAi9iNgxmO5duZwZ4MKm"
api_secret="C4F02SD5SKnS579Ps5iynD3iuNY40cHEpDDCEufRpZ4DrvRvQ0kgOWzsLPYowE6Z"

storage_ticker="BTC"

class Exchange:

    def __init__(self):
      self.client = Client(api_key, api_secret)

    def get_asset(self, assetName):
        tickers = self.client.get_symbol_info(symbol=assetName)
        return tickers

    def buy_asset(self, assetName):
        # Set asset name according mapper CoinMarketCap vs Binance
        assetName = self.mapper(assetName)

        # Get free balance to trade
        result = self.client.get_asset_balance(asset=storage_ticker)
        freebalance = result["free"]

        # Get price asset vs storage ticker
        result = self.client.get_symbol_ticker(symbol=assetName + storage_ticker)
        price = result["price"]

        # Max quantity to buy
        quantity = (freebalance / price) * 0.95

        # Submit a buy order
        order = self.client.order_market_buy(symbol=assetName + storage_ticker, quantity=quantity)

    def sell_all_assets(self):
        response = self.client.get_account()
        balanceLenght = len(response["balances"])
        for i in range(0, balanceLenght):
            item = response["balances"][i]
            if (float(item["free"]) > 0):
                try:
                    order = self.client.order_market_sell(symbol=item["asset"] + storage_ticker, quantity=item["free"])
                except Exception as e:
                    print(e)
                    pass

    def mapper(self, assetName):
        if (assetName == "BTC"):
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
