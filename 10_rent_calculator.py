rent=int(input("Enter House rent:"))
electic_bill=float(input("Enter electric bill: "))
wifi_bill=int(input("enter wifi bill:"))
day_of_ordering_food=int(input("enter how many days you ordered foods:"))
food_total=0
for day in range(1,day_of_ordering_food+1):
    food_snack=int(input("enter food prize:"))
    food_total+=food_snack
food_total_prize=food_total
member=int(input("Enter members:"))
total_spent=rent+electic_bill+wifi_bill+food_total_prize
spent_per_person=total_spent/member
print(f"Total spent is {total_spent:.2f} and spent per member {spent_per_person:.2f}")
