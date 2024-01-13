# Make a closure!

# Outter function takes a func that doubles num
# Inner function takes a num
# If num is even, return the result of passing in num to func
# if num is odd, return None


def outter(func):
    def inner(num):
        if num % 2 == 0:
            return func(num)
        else:
            return None

    return inner


def doubler(num):
    return num * 2


inner = outter(doubler)
print(inner(2))  # 4
print(inner(3))  # None
print(inner(4))  # 8
