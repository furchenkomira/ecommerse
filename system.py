class Product:
    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for index, item in enumerate(self.items, start=1):
                product = item["product"]
                quantity = item["quantity"]
                print(f"{index}. {product.name} - Price: ${product.price} - Quantity: {quantity}")

def main():
    products = [
        Product(1, "Laptop", 800, "Powerful laptop for work and gaming."),
        Product(2, "Smartphone", 500, "High-end smartphone with a stunning camera."),
        Product(3, "Headphones", 100, "Wireless headphones with noise-cancelling technology."),
        Product(4, "Tablet", 300, "Versatile tablet for entertainment and productivity."),
    ]

    cart = ShoppingCart()

    while True:
        print("\nE-commerce Menu:")
        print("1. Browse Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available Products:")
            for product in products:
                print(f"{product.id}. {product.name} - Price: ${product.price}")
        elif choice == "2":
            product_id = int(input("Enter the ID of the product to add to the cart: "))
            quantity = int(input("Enter the quantity: "))
            product = next((p for p in products if p.id == product_id), None)
            if product:
                cart.add_item(product, quantity)
                print(f"{quantity} {product.name} added to the cart.")
            else:
                print("Invalid product ID.")
        elif choice == "3":
            cart.view_cart()
            print(f"Total: ${cart.calculate_total()}")
        elif choice == "4":
            if cart.items:
                print("Checkout completed. Thank you for your purchase!")
                break
            else:
                print("Your cart is empty. Please add items before checking out.")
        elif choice == "5":
            print("Exiting the E-commerce System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
