# points 1: use csv.reader to read data row by row, each row in dict type
# points 2: split data by some patterns, e.g. ';'
# points 3: collect data by collection.counter
# points 4: use horizontal bar (barh), data.reverse()


import csv
import numpy as np
import pandas as pd
import requests
from collections import Counter
from matplotlib import pyplot as plt

# # How to scrap data online
# csv_url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv'
# # csv_data are saved as *downloaded.csv* in current work directory
# response = requests.get(csv_url)
# url_content = response.content
# csv_file = open('downloaded.csv', 'wb') # downloaded.csv
#
# csv_file.write(url_content)
# csv_file.close()

# df = pd.read_csv(csv_url)     #* problem is from permission in webpage downloading*
# data = pd.read_csv('downloaded.csv')
# print(data.shape)
# print(data.columns)
# print(data.head(3))
# print(data.index)

# #***************************
# read csv file row by row, row is in dict type
# with open('downloaded.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     row = next(csv_reader)
#     print(row)
#     print(row['LanguagesWorkedWith'])
#     print(row['LanguagesWorkedWith'].split(';'))
#
# # use collection.counter to collect all programming languages row by row
#     language_counter = Counter()
#     print(language_counter)
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))
#     # # print(language_counter)
#     print(language_counter.most_common(15))
# #***************************

#***************************
# see how Counter works
# from collections import Counter
# c = Counter(['Python', 'Javascript'])
# print(c)
# c.update(['C++', 'Python'])
# print(c)
# c.update(['C++', 'Javascript', 'Python'])
# print(c)
#***************************

plt.style.use("fivethirtyeight")

data = pd.read_csv('downloaded.csv')


ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

print(language_counter)
# print(type(language_counter)) # not dict type

# for item in language_counter.most_common(5):
#     print(item)
#     print(item[0])
#     print(item[1])

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# # reverse the order of object directly
languages.reverse()
popularity.reverse()

# use horizontal bar for better view
plt.barh(languages, popularity)
# plt.bar(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f