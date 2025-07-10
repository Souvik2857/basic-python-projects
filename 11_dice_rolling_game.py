from random import randint
roll_dice=0
times_roll=0
while True:
    start=input("Do you want to play Dice game?(Y/N): ")
    if start.lower()=="y":
        plays=int(input("Enter How many dice you want to roll?\n"))
        times_roll+=1
        list=[]
        for i in range(1,plays+1):
            dice=randint(1,6)
            list.append((dice))
        roll_dice+=plays
        print(f"{list}")
    elif start.lower()=="n":
        print(f"Total Dice rolls are {roll_dice}")
        print(f"Total times of dice rolls {times_roll}")
        print("Thanks for playing....")
        print("Closing the programm....")
        break
    else:
        print("Invalid Input!")
