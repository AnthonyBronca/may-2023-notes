class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def change_make(self, new_make):
        self.make = new_make

    def __repr__(self):
        return f"Car: ({self.make}, {self.model})"


civic = Car("Honda", "Civic")


civic.change_make("Nissa")


print(civic)
