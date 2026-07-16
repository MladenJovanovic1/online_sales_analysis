class Cart:
    
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        total = 0

        for product in self.cart_items:
            total += product.price

        return total
    
    def display_cart(self):
        print("\nSadrzaj korpe:")

        for product in self.cart_items:
            print(f"{product.name} - {product.price} RSD")