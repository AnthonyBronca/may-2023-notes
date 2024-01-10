
# DICTIONARIES

meals = {
    "breakfast": "coffee",
    "lunch": "pizza",
    "dinner": "wings",
    "dessert": "pie",
    4: "meals",
}

# print(meals)
# print(meals[4])
# print(meals["breakfast"])

# # print(meals["second breakfast"])

# print(meals.get("second breakfast", 'NO KEY FOR YOU!!!'))

# if meals.get("second breakfast") is None:
#     meals["second breakfast"] = "apple"
# else:
#     print("Key already exists!")

# print(meals)

# meals["second breakfast"] = "taters"

# print(meals)

# del meals["lunch"]
# print(meals)
# meals.update({"elevensies": "waffle", "supper": "whole turkey"})
# print(meals)

# print("dinner" in meals)
# print("brinner" in meals)

# print(meals.keys())
# print(meals.values())
# print(meals.items())

# for key in meals.keys():
#     print(key)

# for key, val in meals.items():
#     print(key, val)

# SET OPERATIONS
set_1 = {1,2,3}
set_2 = {3,4,5}
set_3 = {1,2,5}

print('UNION', set_1 | set_2 | set_3)         # and
print('INTERSECTION', set_1 & set_2)          # xand
print('DIFFERENCE',  set_2 - set_3)           # or
print('SYMETRICAL DIFFERENCE', set_1 ^ set_2) # xor

a = {0, 1, 2, 3}
b = {2, 3, 4, 5}


#UNION
# print( a | b )
# print(a.union(b))


# INTERSECTION
# print(a & b)
# print(a.intersection(b))

#DIFFERENCE
# print(a - b)
# print(a.difference(b))
# print(b - a)

# SYMMETRIC DIFFERENCE
print(a ^ b)
print(a.symmetric_difference(b))
