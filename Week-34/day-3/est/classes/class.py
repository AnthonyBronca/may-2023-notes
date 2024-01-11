# class Human:
#     def __init__(self, name):
#         self.name = name

#     def change_name(self, new_name):
#         self.name = new_name

#     # def __repr__(self):
#     #     print(f"{self.items()}")
#     # print(f"Human: {self.name}")


# anthony = Human("Anthony")

# print(anthony)

# anthony.change_name("bob")

# print(vars(anthony))


class Creature:
    def __init__(self, name):
        self._name = name

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, new_name):
        self._name = new_name


class Goblin(Creature):
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color

    # Getter for color green
    @property
    def color(self):
        return self._color

    # Setter for changing color
    @color.setter
    def color(self, new_color):
        self._color = new_color

    @classmethod
    def make_goblins(cls, list_of_goblins):
        return [cls(name, color) for name, color in list_of_goblins]

    @staticmethod
    def say_boo():
        print("BOO I am a goblin! Fear me!")


new_goblins = [("Red_goblin", "red"), ("Orange_goblin", "orange")]


red_globin, orange_goblin = Goblin.make_goblins(new_goblins)

red_globin.say_boo()

orange_goblin.say_boo()

print(red_globin.name)

green_goblin = Goblin("Green_Goblin", "green")

green_goblin.say_boo()

# green_goblin.name = "Verde_Goblin"

# print(green_goblin.name)


# green_goblin.color = "red"

# print(green_goblin.color)

# Centaur = Creature("Thanos")


# print(Centaur.name)

# Centaur.name = "Joe"

# print(Centaur.name)

# print(Centaur)

# Rename Thanos to be Joe

# print(vars(Centaur))
