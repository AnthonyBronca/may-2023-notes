# Use a dict comprehension to make a new dict where it only
# has even keys, and their values are doubled from og
# Must be a one liner


# Even keys, means we have to filer -> should have an if conditional AFTER the for loop

og_dict = {1: 10, 2: 20, 3: 30, 4: 40}


def even_dict_doubler(dict1):
    return {key: val * 2 for key, val in dict1.items() if key % 2 == 0}


print(even_dict_doubler(og_dict))  # {2: 40, 4: 80}
