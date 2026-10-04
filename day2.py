item1 = int(input("Enter price of item 1: "))
item2 = int(input("Enter price of item 2: "))

subtotal = item1 + item2
discount = subtotal * 15 / 100
after_discount = subtotal - discount
delivery = 99
total = after_discount + delivery

print("Item 1:",item1 )
print("Item 2:", item2)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Delivery Fee:", delivery)
print("Final Total:", total)