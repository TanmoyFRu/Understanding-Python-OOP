from item import Item
# from phone import Phone

item1 = Item("MyItem", 750, 1)
print(item1.name)

item1.apply_increment(0.2)
print(item1.price)

item1.apply_discount()
print(item1.price)

Item.instantiate_from_csv()
print(Item.all)

item1.apply_discount()
print(item1.price)

item1.pay_rate = 0.7
item1.apply_discount()
print(item1.price)

print(Item.__dict__)  # all the attribute from class level
print(item1.__dict__)  # all attribute from  instance level