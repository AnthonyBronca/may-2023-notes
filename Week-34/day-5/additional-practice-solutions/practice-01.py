# Make a while loop to print everything in the list


print_me = ["hello", "world", "good", "bye", "world"]


def while_print(lst):
    i = 0
    while i < len(lst):
        el = lst[i]
        print(el)
        i += 1
    pass


while_print(print_me)
# hello
# world
# good
# bye
# world
