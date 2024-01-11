class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = {
            "carrots": {"price": 4, "quantity": 10},
            "apples": {"price": 3, "quantity": 5},
            "eggs": {"price": 20, "quantity": 10},
            "bananas": {"price": 7, "quantity": 20},
            "bread": {"price": 5, "quantity": 40},
        }

    def transaction(self, bank, cart):
        total_cost = 0
        for i in range(len(cart)):
            user_cart = cart[i]
            for item in user_cart:
                # print(user_cart, "this is item")
                if item in self.inventory:
                    if self.inventory[item]["quantity"] < user_cart[item]:
                        print(
                            f"We only have {self.inventory[item]['quantity']} of {item}"
                        )
                    else:
                        for i in range(int(user_cart[item])):
                            self.inventory[item]["quantity"] -= 1
                            total_cost += self.inventory[item]["price"]
                else:
                    print(f"We do not have {item} at this store")

        bank.withdraw(total_cost)
        # cart.reset()
        return total_cost

    def get_store(self):
        print(f"{self.name}")
        for item in self.inventory:
            print(
                f"{item}: price: ${self.inventory[item]['price']}, In Stock: {self.inventory[item]['quantity']}"
            )

    def __repr__(self):
        return f"{self.name}, {self.inventory}"
