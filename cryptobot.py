from best_asset import *
from best_asset_test import *


print("CryptoBot v.2.0.0 started")

# HOUR
hour5 = BestAssetTest(PeriodRange.HOUR)
hour10 = BestAssetTest(PeriodRange.HOUR)
hour20 = BestAssetTest(PeriodRange.HOUR)
hour5.run()
# hour10.run()
# hour20.run()

# DAY
day5 = BestAssetTest(PeriodRange.DAY)
day10 = BestAssetTest(PeriodRange.DAY)
day20 = BestAssetTest(PeriodRange.DAY)
# day5.run()
# day10.run()
# day20.run()

# WEEK
week5 = BestAssetTest(PeriodRange.WEEK)
week10 = BestAssetTest(PeriodRange.WEEK)
week20 = BestAssetTest(PeriodRange.WEEK)
# week5.run()
# week10.run()
# week20.run()
