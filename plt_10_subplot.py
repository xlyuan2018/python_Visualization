import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# plt.gcf() # get current figure
# plt.gca() # get current ax
#
#
#
# data = pd.read_csv('data10.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']
#
# # # use object oriented approach
# # fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
# # # following plt.plot can be replaced as ax.plot
#
# plt.plot(ages, py_salaries, label='Python')
# plt.plot(ages, js_salaries, label='JavaScript')
#
# plt.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
#
# plt.legend()
# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
#
#
# plt.tight_layout()
#
# plt.show()





# import pandas as pd
# from matplotlib import pyplot as plt
#
# plt.style.use('seaborn')
#
# data = pd.read_csv('data10.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']


# use object oriented approach
fig, ax = plt.subplots(nrows=2, ncols=2)

print(ax)


#
# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
#
# ax1.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
#
# ax2.plot(ages, py_salaries, label='Python')
# ax2.plot(ages, js_salaries, label='JavaScript')
#
# ax1.legend()
# ax1.set_title('Median Salary (USD) by Age')
# ax1.set_ylabel('Median Salary (USD)')
#
# ax2.legend()
# ax2.set_xlabel('Ages')
# ax2.set_ylabel('Median Salary (USD)')
#
# plt.tight_layout()
#
# plt.show()

# fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')