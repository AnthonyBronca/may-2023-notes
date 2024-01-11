def enter_pin(func):
    def inner(bank, amt):
        inp = input("Please enter your bank pin:    ")
        if int(inp) == bank.pin:
            func(bank, amt)
        else:
            raise Exception("You are not authorized to perform this action")

    return inner
