from random import choice


students_f = open("students.txt", "r")
last_student = open("lastpick.txt", "r").read()
last_pick = open("lastpick.txt", "a")


names = students_f.read()

names_list = names.split("\n")

names_list.remove("")

# filtered_names = list(filter(lambda name: name != "", names_list))


def pick_person(names_list, last_person):
    current_person = choice(names_list)
    if last_person == "":
        last_pick.write(f"\n {current_person}")
        return current_person
    elif last_person == current_person:
        return pick_person(names_list, current_person)
    else:
        last_pick.write(f"\n {current_person}")
        return current_person


def start():
    last = last_student.split("\n")[-1]
    # current_person = pick_person(filtered_names, last_person)
    current_person = pick_person(names_list, last)
    print(current_person)


start()
