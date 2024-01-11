# imports
from models import User, Bank, Cart, Store

# from models.user import User
# from models.bank import Bank

# from .helpers import enter_pin

"""
GOAL: Grab relevant imports to do the following

1. Create a new user in this file passing in the name Anthony
    - Set their bank account to be an instance of bank
2. Create a new bank account in this file starting with $100
    - Create a getter method that allows you to get the pin back
    - Create an setter instance method that allows you to set a pin
    - have an instance method that lets someone enter their password.
        - returns True if they enter it correctly
        - False if they dont
    - have an instance method called "deposit" which adds money
    - have an instance method called "withdraw" which removes money
        - If you try to withdraw more $ than you have, you should raise an
        exception that says "You do not have enough money to withdraw $amount"
        - import the "enter_pin" wrapper that requires a user to enter pin on
        puchases before withdrawing
            - If a user enters a bad pin, raise an exception
            - If a user enters a good pin, try to process the withdrawl
3. Create a new grocery store in this file called Target
    - It will have a default of items
4. Import the helper function "transaction" that helps process purchases
    - It should take in a Bank account and process the payments
    - It should prompt user to enter pin
    - It will withdraw money, subtract the specified quanitity of items
    - It will not process transaction if user does not have enough money

"""

anthony = User("Anthony")
bank1 = Bank(100)
anthony.bank = bank1
print(anthony)
# bank1.change_pin()
# print(bank1.pin)
# bank1.withdraw(7)

target = Store("Target")
cart1 = Cart()
target.get_store()
print("\n", "\n", "----------------", "\n", "\n")
cart1.add_to_cart("apples", 3),
cart1.add_to_cart("bananas", 5),
cart1.add_to_cart("bread", 4),
cart1.add_to_cart("eggs", 1),

print(cart1)
target.transaction(bank1, cart1)

print("\n", "\n", "----------------", "\n", "\n")
target.get_store()
print("\n", "\n", "----------------", "\n", "\n")
print(anthony)
print(cart1)
