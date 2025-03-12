from src.base_order_cat import BaseOrderCat


class Order(BaseOrderCat):
    name: str
    quantity: int
    total_cost: float

    def __init__(self, name, quantity, total_cost):
        self.name = name
        self.quantity = quantity
        self.total_cost = total_cost

    def __str__(self):
        return f"{self.name}, количество товара: {self.quantity}, итоговая стоимость: {self.total_cost}"
