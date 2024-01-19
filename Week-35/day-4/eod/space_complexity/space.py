# Run this file with python3

import matplotlib.pyplot as plt


def create_list(n):
    return [i for i in range(n)]


# create an empty list to store space usage
space_usage = []

for i in range(100):
    # call the create_list function with an increasing value of n
    lst = create_list(i)
    # append the size of the list to the space_usage list
    space_usage.append(lst.__sizeof__())

# create a line plot of space usage over time
plt.plot(space_usage)
plt.xlabel("Function call")
plt.ylabel("Space usage (bytes)")
plt.title("Growth of space usage when creating new lists")
plt.show()
