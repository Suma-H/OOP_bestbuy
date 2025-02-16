from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        """
        Initialize a Store instance.
        :param products: List of Product instances available in the store
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Add a new product to the store.
        :param product: Product instance to add
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the store.
        :param product: Product instance to remove
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all products in the store.
        :return: Total quantity of all active products
        """
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[Product]:
        """
        Get a list of all active products in the store.
        :return: List of active Product instances
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Process an order based on a shopping list.
        :param shopping_list: List of tuples (Product, quantity)
        :return: Total price of the order
        :raises ValueError: If any product quantity is insufficient
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
