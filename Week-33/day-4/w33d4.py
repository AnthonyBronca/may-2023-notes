# FUNCTIONS
# def is_even(num):
#     """returns if the provided number is even or not"""
#     return num % 2 == 0


# # print(is_even(7))

# even = lambda num: num % 2 == 0
# print(even(7))

# multiply = lambda num1, num2: num1 * num2

# print(multiply(3,4))


# SCOPE
# y = 200
# PII = 3.145

# print("y in global scope", y)
# def some_function():
#     # y = 10
#     global y
#     print("y inside the function", y)
#     print(PII)
#     if True:
#         print("in if block", y)
#         y += 10
#         print("in if block", y)
#     y += 10
#     print("y inside the function second time", y)


# some_function()

# print("y in global scope", y)


# LISTS
dinners = ["pizza", "wings", "steak", "cobb salad", "taco"]
# print(dinners)
# print(len(dinners))

# print(dinners[2])
# print(dinners[1::2])
# print(dinners[::-1])
# dinners.append("turkey")
# print(dinners)
# dinners.extend(["sloppy joe", "corn"])
# print(dinners)
# dinners.insert(1, "shrimp")
# print(dinners)
# dinners.remove("taco")
# print(dinners)
# dinners.pop(1)
print(dinners)
dinners.sort()
print(dinners)

vals = [2, 4, 45, 12, 234]
print(sum(vals))
print(min(vals))
print(max(vals))
