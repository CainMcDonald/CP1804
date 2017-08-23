number_of_items = int(input("Please enter the number of items total: "))
new_price = 0
while number_of_items < 0:
    print("Invalid Number")
    number_of_items = int(input("Please enter the number of items total "))
for i in range(number_of_items):
    item_price = float(input("Please enter your next items price: "))
    new_price += item_price
if new_price >= 100:
    bonus = new_price * 0.1
    new_price_bonus = new_price - bonus
    print("Total cost: ${:.2f} Total number of item {}".format(new_price_bonus, number_of_items))
else:
    print("Total cost: ${:.2f} Total number of item {}".format(new_price, number_of_items))
