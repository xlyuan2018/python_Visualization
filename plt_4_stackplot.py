from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


# minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# example: How programmers are working on the project
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(hours, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05)) # coordinates pass on a tuple
# plt.legend(loc=('upper left'))
# plt.legend(loc=('lower left'))

plt.title("My Awesome Stack Plot")
plt.xlabel('Hours')
plt.tight_layout()
plt.show()
