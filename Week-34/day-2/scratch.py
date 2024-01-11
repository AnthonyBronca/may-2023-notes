
"""
Dictionaries


Basically work like objects in Javascript

Key differences:

As of Python 3.7, dictionaries are now insertion ordered
 - Note this would be unordered if older version is used

vs

Javascript objects are never guaranteed to be in order

-----

Keys can be strings, nums, tups, booleans (immutable items)
but string NEED double quotes

vs

Javascript does not need quotes for keys, javascript needs keys to be strings
or it converts the key to a string


-----

Look up needs bracket notations. dot notation can only work for methods
in classes

vs

Javascript: methods can exist in objects, and you can use dot notation +
bracket notation to key into stuff

----

Deleting a key:value pair in python uses 'del' keyword

vs

Javascript: uses 'delete' key word


"""
# Movie theatre example


# my_movie_theatre = {
#     "name": "Cinemark 24",
#     "showing": ["dark night", "iron man", "avengers"],
#     "occupancy": {
#         1: 210,
#         2: 150,
#         3: 100
#     },
#     "delete": "delete this"
# }






# del my_movie_theatre["delete"]


# # print(my_movie_theatre)

# # ----------------------------------

# # Dictionary comprehension

# movies = {x:x.upper()  for x in my_movie_theatre["showing"]}

# # print(movies)



# """

# Sets:

# 1. mutable, unordered, all elements unique
# 2. sets use curlies (dont confuse them with JS syntax)
# 3. Look like dictionaries but have no key:values
# """

# movie_list = set(movies)

# movie_list.add("Anthony")


# my_movie_theatre["showing"] = movie_list



# # Object.keys(obj)

# new_movies_list = [
#     "Charlie and the chocolate factory",
#     "Hunger games",
#     "Grinch",
#     "Anthony"
# ]

# new_movies = {movie for movie in new_movies_list}
# print(new_movies)
# print(movie_list)

# # print(my_movie_theatre)


# current_shows = {movie for movie in new_movies & movie_list}
# print(current_shows)
# Set comprehension -> tip: looks like dict comprehension without the val




# Set operations

# Sort vs Sorted
# SORT MUTATED A LIST




lst = [2,1,3]

test = sorted(lst)
# test = lst.sort()
print(lst)
print(test)
