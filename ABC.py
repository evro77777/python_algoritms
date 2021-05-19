from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total_all(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    # то, что причитается
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total_all() - discount

    def __repr__(self):
        return f'Order total:{self.total_all()},due : {self.due()}'


class Promotion(ABC):
    @abstractmethod
    def discount(self):
        """Вернуть скидку в виде положительной суммы в долларах"""
        pass


class FidelityPromo(Promotion):
    """5% скидка для зазазчиков, имеющих не менее 1000 баллов лояльности"""

    def discount(self):
        return self.total_all() * .05 if self.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """10% скидка для каждой позиции LineItem, в которой заказано не менее 20 единиц"""

    def discount(self):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    """7% скидка для заказов, включающих не менее 10 различных позиций"""

    def discount(self):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('wmelon', 5, 5)]
order = Order(joe, cart, FidelityPromo)
order2 = Order(ann, cart, FidelityPromo)
print(order)
print(order2)
