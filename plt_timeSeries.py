from matplotlib import pyplot as plt

import pandas as pd
import requests

df = pd.read_csv('ETH_1h.csv')
print(df.shape)

# # create a function to parse the date format
# d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
# # use parse function to change the date format while reading csv data
# df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser = d_parser)
# print(df.shape)



# print(df.loc[0, 'Date'].day_name())
df['DayOfWeek'] = df['Date'].dt.day_name()
# print(df.head())

# create filter
filt = (df['Date'] >= '2019') & (df['Date'] < '2020')

# filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
# print(df.loc[filt])
# print(pd.to_datetime('2019-01-01'))
df.set_index('Date', inplace = True)
print(df)
#
# print(df.loc['2019'])
# print(df.loc['2020-01': '2020-02'])

# get data in daily basis
# print(df.loc['2020-01': '2020-02'].head(24))

print(df.loc['2020-01-01']['High'].max())

# # resampling on dates
# print(df['High'].resample('D').max())
# print(df['High'].resample('W').max())
# print(df['High'].resample('M').max())
# print(df['High'].resample('Y').max())

highs = df['High'].resample('M').max()
highs.plot()

# aggregation on multiple columns
print(df.resample('W').agg({'High': 'max', 'Low': 'min', 'Open': 'mean', 'Close': 'mean', 'Volume': 'mean'}))

df1 = df.resample('W').agg({'High': 'max', 'Low': 'min', 'Open': 'mean', 'Close': 'mean'})
df1 = df1.rename(columns={
    'High': 'high_max',
    'Low': 'low_min',
    'Open': 'open_mean',
    'Close': 'close_mean'
})
print(df1.head(3))
df1.plot()

plt.tight_layout()
plt.show()