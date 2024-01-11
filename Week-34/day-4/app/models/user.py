class User:
    def __init__(self, name):
        self._name = name
        self._bank = None

    @property
    def name(self):
        return self._name

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, bank_class):
        self._bank = bank_class

    def __repr__(self):
        return f"User: {self.name}, {self.bank}"
