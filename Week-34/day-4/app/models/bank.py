# imports
from helpers import enter_pin


class Bank:
    def __init__(self, start_amt):
        self.balance = start_amt
        self._pin = 0000

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, new_pin):
        self._pin = new_pin

    def change_pin(self):
        if self.pin == 0000:
            new_pin = input("Please enter a new pin:     ")
            self.pin = new_pin
        else:
            old_pin = input("Please enter your current pin:     ")
            if old_pin == self.pin:
                new_pin = input("Please enter a new pin:     ")
                self.pin = new_pin
            else:
                print("You did not enter a correct pin. Please try again.")
                return self.change_pin()

    def deposit(self, amt):
        self.balance = amt

    @enter_pin
    def withdraw(self, amt):
        try:
            if amt > self.balance:
                raise Exception(f"You do not have enough withdraw {amt}")
            else:
                self.balance = self.balance - amt
        except Exception as e:
            print(f"ERROR: {e}")

    def __repr__(self):
        return f"Bank: (balance: ${self.balance}, pin: ****)"
