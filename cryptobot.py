import schedule
import time
from pprint import pprint
from exchange import *
from statistics import *
from asset_vs_btc import *
from best_asset import *


print("CryptoBot v.1.0.0 started")

# HOUR
hour5 = BestAsset(PeriodRange.HOUR, 5)
hour10 = BestAsset(PeriodRange.HOUR, 10)
hour20 = BestAsset(PeriodRange.HOUR, 20)
hour5.run()
# hour10.run()
# hour20.run()

# DAY
day5 = BestAsset(PeriodRange.DAY, 5)
day10 = BestAsset(PeriodRange.DAY, 10)
day20 = BestAsset(PeriodRange.DAY, 20)
# day5.run()
# day10.run()
# day20.run()

# WEEK
week5 = BestAsset(PeriodRange.WEEK, 5)
week10 = BestAsset(PeriodRange.WEEK, 10)
week20 = BestAsset(PeriodRange.WEEK, 20)
# week5.run()
# week10.run()
# week20.run()
