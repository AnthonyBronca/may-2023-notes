
names = ["anthony", "andrew", "bill", "edward", "arnold", "charles"]

# filtered_list = list(filter(lambda el: el == "anthony", names))

# print(filtered_list)

# Use filter to create a NEW list of names that start with 'a'


# a_names = list(filter(lambda el: el[0].lower() == 'a', names))

# print(a_names)

# ----------------------
# Use map to create a NEW list, where all the names are upper cased

# arr = [1, 2, 3]


# def call_back(el):
#     return el * 2
# names = ["anthony", "andrew", "bill", "edward", "arnold", "charles"]

# upper_names = list(map(lambda el: el * 2, arr))

upper_names = list(map(lambda el: el.upper(), names))

# print(upper_names)


# ----------------------

# use sorted to create a NEW list where names are in alphabetical order


in_order = sorted(names)

# print(in_order)

# ----------------------

# use sorted with a key to sort in alphetical looking at last letter
# in name istead of first:
# res -> ["edward", "arnold", "bill", "charles", " andrew", "anthony"]
# Hint: Try using a helper func


last_name_order = sorted(names, key=lambda name: name[-1])


# print(last_name_order)


# HELP ME SOLVE THIS USING A LAMBDA INSTEAD! ^

# ----------------------

# Use "all" to return true if all the names are lowercased
# Hint: try passing in an advanced list method

names = ["anthony", "andrew", "bill", "edward", "arnold", "charles"]

# test = map(lambda name: name == name.lower(), names)
# all_lowered = all(map(lambda name: name == name.lower(), names))
# print(test)
# print(all_lowered)


# Use "any" to return False i none of the names start with "J"

# any_js = any(map(lambda name: name[0].upper() == "J", names))


# print(any_js)


# TRY THIS OUT BELOW

"""
Write a function that filters this list to remove all numbers that are odd.
Use the built in Filter method. Use a Lambda function to solve this


numbers = [1,2,3,4,5,6,7,8,9]
Answer should look like: [2,4,6,8]


"""


"""
Write a function that gets the multiple of 5 for each el in this list
Use the built in map method. Use a Lambda function to solve this

numbers2 = [1,2,3,4,5]

Answer should look like: [5, 10, 15, 20, 25]


"""

"""
Write a function that returns True if all the numbers in the numbers2 problem above are odd
Use the built in all method.



Answer should look like: False


"""


"""
Write a function that returns True if any of the numbers in the numbers2 problem above are greater than 20
Use the built in any method.



Answer should look like: True

"""


"""
Write a function called my_sort that takes in a list of tuples. It should
sort the list, out of place and return a new list, where all items are
sorted based on the last element of a tuple

HINT: you may need to use the 'key' key word

lst1 = [(1,2,3), (3,2,1), (2,2,2)]
lst2 = [('a', 'b', 'c'), ('d','b'), ('a')]

my_sort(lst1) # [(3,2,1), (2,2,2), (1,2,3)]
my_sort(lst2) #[('a'), ('d','b'), ('a','b','c')]
"""
