import schedule
import time
from pprint import pprint
from exchange import *
from statistics import *
from asset_vs_btc import *
from best_asset import *


print("CryptoBot v.1.0.0 started")

aux = BestAsset(PeriodRange.HOUR, 500)
aux.run()

# aux = AssetVsBtc("ethereum")
# aux.run()
