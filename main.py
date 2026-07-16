from product import Product
from product_manager import ProductManager


manager = ProductManager()

product1 = Product("Laptop", 1200, 5)
product2 = Product("Mis", 25, 15)
product3 = Product("Monitor", 300, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.display_products()

print("Ukupna vrednost inventara:")
print(manager.total_inventory_value())
