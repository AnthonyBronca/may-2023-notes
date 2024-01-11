class Game:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score * 10


# my_game = Game()
# print(my_game.score)  # 0

# my_game.score = 5
# print(my_game.score)  # 50

# -------------------------


class Quadrilateral:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Quadrilateral):
    def __init__(self, length, width):
        if length != width:
            raise Exception("A square must have an equal length and width.")

        super().__init__(length, width)


# quad = Quadrilateral(20, 10)
# print(f"{quad.length}, {quad.width}")  # 20, 10

# square = Square(10, 10)
# print(f"{square.length}, {square.width}")  # 10, 10

# not_square = Square(5, 10)  # Exception: A square must have an equal length and width.


# -------------------------


class StrNumeric:
    def __init__(self, value):
        if isinstance(value, str) and not value.isnumeric():
            raise Exception("String value can have only numeric characters.")
        self.val = value

    def __add__(self, thing2):
        return int(self.val) + int(thing2)


# str_1 = StrNumeric("1")
# print(str_1 + 2)  # 3

# str_44 = StrNumeric("44")
# print(str_44 + 6)  # 50

# num_44 = 44
# print(num_44 + 6)  # 50

# not_numeric = StrNumeric(
#     "1.2"
# )  # Exception: String value can have only numeric characters.


# -------------------------


def hello_world_decorator(func):
    def inner():
        print("Hello")
        func()
        print("Goodnight")

    return inner


@hello_world_decorator
def world():
    print("World")


world()  # > Hello World Goodnight
