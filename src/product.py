class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product, prod_list):
        for prod in prod_list:
            if prod.name == new_product["name"]:
                prod.quantity += new_product["quantity"]
                if prod.price < new_product["price"]:
                    prod.price = new_product["price"]
                return prod

        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price == 0 or price < 0:
            print("Цена не должна быть нулевая или отрицательная")
        if 0 < price < self.__price:
            request_for_downgrade = input("Согласны ли вы на понижение цены (y - 'да', другой ответ - 'нет')?: ")
            if request_for_downgrade == "y":
                self.__price = price
            else:
                self.__price = self.__price
