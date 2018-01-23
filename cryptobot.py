import schedule
import time
from pprint import pprint
from exchange import *
from statistics import *
from asset_vs_btc import *
from best_asset import *
from best_asset_test import *


print("CryptoBot v.1.0.0 started")

# HOUR
hour5 = BestAssetTest(PeriodRange.HOUR, 5)
hour10 = BestAssetTest(PeriodRange.HOUR, 10)
hour20 = BestAssetTest(PeriodRange.HOUR, 20)
hour5.run()
# hour10.run()
# hour20.run()

# DAY
day5 = BestAssetTest(PeriodRange.DAY, 5)
day10 = BestAssetTest(PeriodRange.DAY, 10)
day20 = BestAssetTest(PeriodRange.DAY, 20)
# day5.run()
# day10.run()
# day20.run()

# WEEK
week5 = BestAssetTest(PeriodRange.WEEK, 5)
week10 = BestAssetTest(PeriodRange.WEEK, 10)
week20 = BestAssetTest(PeriodRange.WEEK, 20)
# week5.run()
# week10.run()
# week20.run()
