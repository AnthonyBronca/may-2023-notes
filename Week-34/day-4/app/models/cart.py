class Cart:
    def __init__(self):
        self.cart = []

    def reset(self):
        self.cart = []

    def add_to_cart(self, item, amount):
        product = {item: amount}
        self.cart.append(product)

    def get_cart(self):
        return self.cart

    def __repr__(self):
        return f"Cart: ({self.cart})"
