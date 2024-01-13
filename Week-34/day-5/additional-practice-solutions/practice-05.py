# take a list of lists and removes elements from nested-lists
# where the product of el tripled is not even
# Solve this using map, lambda, and list comprehension
# Must be a one-liner

double_lists = [[1], [2, 3], [4, 5, 6]]
"""
Explanation:
1 * 3 = 3 -> []
2 * 3 = 6 and 3 * 3 = 9 -> [2]
4 * 3 = 12 and 5 * 3 = 15 and 6 * 3 = 18 -> [4,6]
res = [[], [2], [4,6]]


"""


def doubler_lists(lst):
    pass


print(doubler_lists(double_lists))  # [[], [2], [4,6]]
