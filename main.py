import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(store_obj):
    while True:
        print("\nStore Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for product in store_obj.get_all_products():
                print(product.show())
        elif choice == "2":
            print(f"Total quantity in store: {store_obj.get_total_quantity()}")
        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                quantity = int(input("Enter quantity: "))

                product = next((p for p in store_obj.get_all_products() if p.name == product_name), None)
                if product:
                    shopping_list.append((product, quantity))
                else:
                    print("Product not found. Try again.")

            try:
                total_price = store_obj.order(shopping_list)
                print(f"Order placed successfully! Total cost: ${total_price:.2f}")
            except ValueError as e:
                print(f"Error placing order: {e}")
        elif choice == "4":
            print("Exiting the store. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start(best_buy)
