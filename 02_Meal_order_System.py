print("Welcome to Our Cafe\nThe Best Cafe")
name=input("Enter your name: ")
print(f"Welcome {name}")
print("Here is Our Menu")
menu={
    "Coffee":80,
    "Burger":150,
    "Pizza":250,
    "Sandwitch":50,
    "Pastry":80,
    "Pasta":90,
    "Noodles":40
}
for item,prize in menu.items():
    print(f"{item}-{prize}")
total_order=0
order=input("Enter your order: ").capitalize()
if(order in menu):
    total_order+=menu[order]
else:
    print("item is not available")
    exit()
other_order=input("Do you want to order more?\n(yes/no)")
if other_order=="yes":
    print("enter your order")
    while True:
        orders=input("Add items\n").capitalize()
        if orders.lower()=="exit":
            break
        elif orders in menu:
            total_order+=menu[orders]
        else:
            print("item is not available.Please choose from the menu")
    print(f"Your total order is {total_order}")
    print("Thankyou!")
elif other_order=="no":
    print(f"your total order is {total_order}")
    print("Thankyou!")




          
  