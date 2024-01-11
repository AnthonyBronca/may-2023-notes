# Class for humans
class Human:
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

    # def __repr__(self):
    #     print(f"Human: ({self._name})")


anthony = Human("Anthony")
# print(anthony.name)


# Class for Creatures
class Creature:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# Create Goblin


class Goblin(Creature):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # Decorator fo function that creates goblins
    @classmethod  # Build classes
    def make_goblin(cls, goblin_list):
        return [cls(name, color) for name, color in goblin_list]

    @staticmethod
    def say_boo():
        # Throw new Error
        print("Say boo")
        # raise Exception("This is a boo error")


new_goblins = [("red_goblin", "red"), ("blue_goblin", "blue")]


green_goblin = Goblin("Green_goblin", "green")
# red_goblin = Goblin("red_goblin", "red")
# blue_goblin = Goblin("blue_goblin",  "blue")


red_goblin, blue_goblin = Goblin.make_goblin(new_goblins)

red_goblin.say_boo()
blue_goblin.say_boo()
green_goblin.say_boo()


# for gob in new_class_goblins:
#     print(gob.get_name())

# print(new_class_goblins)
