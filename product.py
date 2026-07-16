class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name}")
        print(f"Cena: {self.price}")
        print(f"Količina: {self.quantity}")
        print("------------------------")

    def update_quantity(self, quantity):
        self.quantity = quantity