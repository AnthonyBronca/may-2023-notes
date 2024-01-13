# Make a list comprehension that doubles all vals
# Must be a one-liner


start_nums = [1, 2, 3, 4, 5]


def doubler(lst):
    return [el * 2 for el in lst]


print(doubler(start_nums))  # [2,4,6,8,10]
