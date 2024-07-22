def process_orders(orders):
    for order in orders:
        name, product, quantity = order  
        print(f"Customer Name: {name}, Product: {product}, Quantity: {quantity}")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Headphones", 3)
]

process_orders(orders)
