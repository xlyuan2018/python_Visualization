# import pandas as pd
# from matplotlib import pyplot as plt
#
# plt.style.use('fivethirtyeight')
#
# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# # bins = 10
# bins = [10, 20, 30, 40, 50, 60]
#
# plt.hist(ages, bins=bins, edgecolor='black')
#
# # data = pd.read_csv('data6.csv')
# # ids = data['Responder_id']
# # ages = data['Age']
#
# # median_age = 29
# # color = '#fc4f30'
#
# # plt.legend()
#
# plt.title('Ages of Respondents')
# plt.xlabel('Ages')
# plt.ylabel('Total Respondents')
#
# plt.tight_layout()
#
# plt.show()



# Example: Age group of people who responded to the survey

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data6.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(ages, bins=bins, edgecolor='black')


median_age = 29
color = '#fc4f30'

# number of respondents on age groups are very different, so using log transformation to make little number visible
plt.hist(ages, bins=bins, edgecolor='black', log=True)
# add verticle line on the ax
plt.axvline(median_age, color=color, label='Age Median', linewidth=2)



plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()