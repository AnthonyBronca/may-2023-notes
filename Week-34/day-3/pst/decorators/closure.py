admins = [
    {"username": "Anthony", "password": "password"},
    {"username": "Will", "password": "password2"},
]


mod6 = {
    "week33": "Intro to Python",
    "week34": "Python",
    "assessment": "Week 34 + 35 Assessment",
}


current_user = {
    "username": input("username?:     "),
    "password": input("password?:     "),
}


# print(current_user)


def deny_access(topic, content):
    print(f"You do not have permission to edit {topic}")


def is_admin(func):
    for admin in admins:
        if current_user["username"] == admin["username"] and (
            current_user["password"] == admin["password"]
        ):
            return func

    else:
        return deny_access


def change_content(topic, content):
    if topic in mod6:
        mod6[topic] = content
        print("Content Modified Successfull!")
    else:
        print("That topic did not exist")


change_item = is_admin(change_content)

change_item("week33", "Hello World")

# change_content("week33", "Hello World")


print(mod6)
