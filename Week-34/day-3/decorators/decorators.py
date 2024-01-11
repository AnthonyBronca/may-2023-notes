admins = [
    {"username": "Anthony", "password": "password"},
    {"username": "Will", "password": "password2"},
]


mod6 = {
    "week33": "Intro to Python",
    "week34": "Python",
    "assessment": "Week 33 and Week 34 Assessment",
}


current_user = {
    "username": input("Username?:     "),
    "password": input("Password?:     "),
}


def deny_access(topic, content):
    print(f"You do not have permission to edit {topic}")


def is_admin(func):
    for admin in admins:
        if current_user["username"] == admin["username"] and (
            current_user["password"] == admin["password"]
        ):
            return func

    return deny_access


# Func that lets us change content
@is_admin
def change_content(topic, content):
    if topic in mod6:
        mod6[topic] = content
        print("Content modified!!")
    else:
        print("That topic did not exist")


# change_content = is_admin(change_content)
change_content("week34", "Hello world")


# change_content("week34", "Hello world")
print(mod6)

# print(current_user)
