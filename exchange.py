import json
from binance.client import Client
from binance.enums import *

api_key="haBYdYkOQxv76sON2X9VFde2eiEp0FM9R09Ofrg7jBgCi4uP0KGW6FrtO3y75xUt"
api_secret="NQeb0Si3dZFDbbBZzDXq1tlmLWyIH34vII9enW93iaKcrCunXZMffjQPFTC4oBDc"

class Exchange:

    def __init__(self):
      self.client = Client(api_key, api_secret)

    def get_asset(self, assetName):
        tickers = self.client.get_symbol_info(symbol=assetName)
        return tickers

    def buy_asset(self, assetName):
        if (assetName != None):
            # order = client.order_market_buy(
            # symbol='ADABTC',
            # quantity=1
            # print("buy: ", assetName)
            test = None

    def sell_asset(self, assetName):
        if (assetName != None):
            # order = client.order_market_sell(
            # symbol='ADABTC',
            # quantity=get_asset_quantity(assetName)
            # print("sell: ", assetName)
            test = None

    def get_asset_quantity(self, assetName):
        response = self.client.get_account()
        balanceLenght = len(response["balances"])
        for i in range(0, balanceLenght):
            item = response["balances"][i]
            if (item["asset"] == assetName):
                return item["free"]
