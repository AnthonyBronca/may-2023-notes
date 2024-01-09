from random import choice



students_f = open("students.txt", "r")

names = students_f.read()

names_list = names.split("\n")

names_list.remove("")


def pick_person(names_list, last_person):
    current_person = choice(names_list)
    if last_person == "":
        last_person = current_person
        return current_person
    elif last_person == current_person:
        return pick_person(names_list)
    else:
        return current_person




def start():
    last_person = ""
    current_person = pick_person(names_list, last_person)
    print(current_person)
