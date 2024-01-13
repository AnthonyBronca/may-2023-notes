# Make a closure!

# Outter function takes a func that doubles num
# Inner function takes a num
# If num is even, return the result of passing in num to func
# if num is odd, return None


def outter():
    pass


def doubler(num):
    return num * 2


inner = outter(doubler)
print(inner(2))  # 4
print(inner(3))  # None
print(inner(4))  # 8
