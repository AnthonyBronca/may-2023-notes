"""
Write a function that filters this list to remove all numbers that are odd.
Use the built in Filter method. Use a Lambda function to solve this


Answer should look like: [2,4,6,8]


"""
numbers = [1,2,3,4,5,6,7,8,9]

res1 =  list(filter(lambda val: val % 2 == 0, numbers))

# print(res1)


"""
Write a function that gets the multiple of 5 for each el in this list
Use the built in map method. Use a Lambda function to solve this


Answer should look like: [5, 10, 15, 20, 25]




"""
numbers2 = [1,2,3,4,5]
res2 = list(map(lambda el: el * 5,numbers2 ))

# print(res2)
"""
Write a function that returns True if all the numbers in the numbers2 problem above are odd
Use the built in all method.



Answer should look like: False

"""

are_odd = all(map(lambda num: num % 2 !=0, numbers2))



# print(are_odd)
"""
Write a function that returns True if any of the numbers in the numbers2 problem above are greater than 20
Use the built in any method.



Answer should look like: True

"""

def greater_than_20(lst):
    return any(map(lambda el: el > 20,lst))




# print(greater_than_20(res2))

"""
Write a function called my_sort that takes in a list of tuples. It should
sort the list, out of place and return a new list, where all items are
sorted based on the last element of a tuple

HINT: you may need to use the 'key' key word

"""



# lst1 = [(1,2,3), (3,2,1), (2,2,2)]
# lst2 = [('a', 'b', 'c'), ('d','b'), ('a',)]


# def my_sort(lst):
#     return sorted(lst, key=lambda tup: tup[-1])

# print(my_sort(lst1)) # [(3,2,1), (2,2,2), (1,2,3)]
# print(my_sort(lst2)) #[('a'), ('d','b'), ('a','b','c')]
