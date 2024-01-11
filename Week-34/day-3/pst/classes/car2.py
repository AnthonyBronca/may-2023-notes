class Car:
    def __init__(self, model, name):
        self._model = model
        self._name = name

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, new_name):
        self._name = new_name


civic = Car("Honda", "Civic")


civic.name = "richa"

print(civic.name)
