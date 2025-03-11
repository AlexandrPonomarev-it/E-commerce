from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        prod_sum = 0
        for prod in self.__products:
            prod_sum += prod.quantity
        return f"{self.name}, количество продуктов: {prod_sum} шт."

    def add_product(self, products: Product):
        if isinstance(products, Product):
            self.__products.append(products)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"

        return products_str

    @property
    def product_in_list(self):
        return self.__products
