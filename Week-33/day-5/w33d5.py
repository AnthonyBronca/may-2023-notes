# TUPLES

# tup = ('red', 'blue')
# tup += ('green', "orange")

# print(tup)

# tup_2 = "Neo", "Trinity", "Morpheus"

# print(tup_2)

# tup_3 = 1,
# tup_4 = 2,
# tup_5 = 3,

# # EMPTY TUPLES
# empty_tuple = ()
# empty_tuple2 = tuple()

# # SINGLETON TUPLE
# tup_6 = (1,)
# tup_7 = 2,


# def sum_and_average(lst):
#     list_sum = sum(lst)
#     average = list_sum / len(lst)
#     return (list_sum, average)


# ran_sum, ran_avg = sum_and_average([1, 2, 3, 4, 5])

# print(ran_avg, ran_sum)



# RANGES
# values = range(start,stop,step)
# vals = range(1,10,2)
# print(vals)
# print(tuple(vals))

lunch = ["wings", "pizza", "turkey", "salmon"]

# for index in range(len(lunch)):
#     print(index, lunch[index])

# more_vals = range(50, 0, -10)
# print(list(more_vals))


# Problem 3 - Factorial
# Write your function, here.
# def factorial(num):
#     total = 1
#     for val in range(1, num + 1):
#         total *= val
#     return total

# print(factorial(1))     #> 1
# print(factorial(8))     #> 40320  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(factorial(12))    #> 479001600

# def recur_fact(num):
#     if num == 1:
#         return num

#     return num * recur_fact(num -1)


# print(recur_fact(1))     #> 1
# print(recur_fact(8))     #> 40320  # [1, 2, 3, 4, 5, 6, 7, 8]
# print(recur_fact(12))    #> 479001600


# COMPREHENSTIONS
# my_list = [1, "2", True, "butter", None]
# my_list_copy = [item for item in my_list]
# print(my_list_copy)
# my_list_copy2 = [*my_list]
# print(my_list_copy)

nums = [-11, -5, 11, 10, 14]

# mapped_comp = [num * 2 for num in nums]
# print(mapped_comp)

# new_list = []
# for num in nums:
#     new_list.append(num * 2)

# print(new_list)

# filtered_comp = [num for num in nums if num > 0]
# print(filtered_comp)

# mapped_and_filtered_comp = [num * 2 for num in nums if num > 0]
# print(mapped_and_filtered_comp)

# names = ['bob', 'jim', 'andrew', 'jane', 'kate']
# cap_comp = [ name.title() for name in names ]
# print(cap_comp)

# users = [user.to_dict() for user in User.query.all()]

# new_list = [return_val for x in iterable if conditional=true]

# users = [
#   {'first_name': 'John', 'last_name': 'Doe', 'membership': 'premium'},
#   {'first_name': None, 'last_name': 'Doe', 'membership': 'premium'},
#   {'first_name': 'John', 'last_name': None, 'membership': 'premium'},
#   {'first_name': 'Jane', 'last_name': 'Smith', 'membership': 'free'},
#   {'first_name': 'Sarah', 'last_name': 'Conner', 'membership': 'free'},
#   {'first_name': 'John', 'last_name': 'Conner', 'membership': None}]
# #                   (return_val             ) (iteration      ) (filter conditional    )
# incomplete_users = [(users.index(user), user) for user in users if None in user.values()]
# #                (return_val                                                   ) (iteration      ) (filter conditional              )
# premium_users = [{'first_name':user['first_name'],'last_name':user['last_name']} for user in users if user['membership'] == 'premium']

# print('Incomplete: ', incomplete_users)
# print('\nPremium: ', premium_users)

# vowels = 'aeiouAEIOU'
# sentence = 'This is a comprehension?'

# sent_vowels = [char for char in sentence if char in vowels]
# print('\nVOWELS:', sent_vowels)
# #        (return value             ) (iteration       ) (filter conditional)
# evens = ['EVEN' if i%2==0 else 'ODD' for i in range(10)]
# print('\nFRONT IF:', evens)
