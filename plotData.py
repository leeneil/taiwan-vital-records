import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'birth_stats.htm.json'
# filename = 'marriage_stats.htm.json'
data = json.load( open(filename) )

print(data[1])
print(data[0])

df = pd.DataFrame( data[1], index=data[0][0] ).T
df.index = pd.to_datetime(df.index, format='%Y-%m')
df.sort_index(inplace=True)


print(df.tail())
print(df.index)

# plt.figure()
# df.plot(y="結婚對數")
# plt.rc('font', family='jf-jinxuan-fresh2.2')
# plt.show()
