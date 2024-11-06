import csv


class Item:
    # class attribute

    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name, price, quantity):
        # run validation for the asserted arguments

        assert price >= 0, f"Price {price} is not greater then or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater then or equal to zero"

        # assign to self object

        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price*increment_value

    @property
    # property decorator  = read-only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Your name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )

    @staticmethod
    # static method doesn't pass object reference as the first argument
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"
        # {self.__class__.__name__} it is responsible for the class name

# Item.instantiate_from_csv()
# print(Item.all)

# for instance in Item.all:
# print(instance.name)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.__dict__)  # all the attribute from class level
# print(item1.__dict__)  # all attribute from  instance level
