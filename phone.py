from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to all attribute/ methods
        super().__init__(name, price, quantity)
        # run validation for the asserted arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater then or equal to zero"
        # assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("JSCPhoneV10", 500, 5, 1)
# phone1.broken_phones = 1
# phone2 = Phone("JSCPhoneV20", 700, 5)
# phone2.broken_phones = 1

print(Item.all)
print(Phone.all)
# print(Item.is_integer(6.5))