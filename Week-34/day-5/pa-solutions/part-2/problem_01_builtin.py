# PROBLEM 1 - BUILT IN LIST METHODS:
#
# Write a function named "filter_small_lists" that accepts an iterable
# containing lists and returns a list of the lists that have more than two
# elements in them.
#
# * NOTE: You must use the builtin "filter" method in your function.
#
#
# In addition to running `pytest test/test_problem_01_builtin.py` you can also
# test your code manually using the sample data below.
#
# ______________________________YOUR CODE BELOW______________________________#


# Your code here

# We take in a list of nested lists
# Return a list, with nested lists that have more than 2 elements per nested list


def filter_small_lists(lst):
    return list(filter(lambda subLst: len(subLst) > 2, lst))


# __________SAMPLE TEST DATA__________ #
# print(
#     filter_small_lists([[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]])
# )  # [[1, 2, 3], [1, 2, 3, 4]]
# print(filter_small_lists([]))  # []
