"""
We can use a list comprehension to make new arrays with one
line of logic. While these can be powerful, also take into
account readability.


TIP:

1. if before for -> replace the el (same size list)

2. if after for -> filter list (makes resulting list smaller)

3. use the same variable for el to reference the el in new list




"""

# Return a new list with all items multiplied by 2

my_num_list = [1, 2, 3, 4, 5]

# return a new list with only 2 -> [2]


# print(only2lst)

# return a new list, replacing all odd numbers with 5


# print(weird_lst)


"""
We can also use list comprehensions through multiple lists at the same time using multiple for..in statements

Lets return a new list with the sum of els in lst1 and els in lst2.

we can do this using evaluations before our loops -> [() for...in for..in]

Ex: [1+4, 1+5, 1+6, 2+4, 2+5, 2+6, 3+4, 3+5, 3+6] -> [5, 6, 7, 6, 7, 8, 7, 8, 9]
"""

lst1 = [1,2,3]
lst2 = [4,5,6]


# print(combined_list)
