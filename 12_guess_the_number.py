#guess the numbe game
import random
computer=random.randint(1,100)
guessed=0
while True: #here true is for infinite loop
    #if i dont write true then it takes input only ones
    my_input=int(input("enter number:"))
    guessed+=1
    if(my_input>computer):
        print("Lower number please!")
        
    elif(my_input<computer):
        print("Higher number please!")
    else:
        print(f"Congratulations!\nYou Guessed the number {computer}")
        print(f"your total guesses is {guessed}")
        break
with open("D:\\Documents\\python programing\\projects\\guess_the_number.txt",'r+') as f:
    f.seek(0) #f.seek to get cursor on first on the text
    data=f.read()
    if(data==""):
        f.seek(0)
        f.write(str(guessed)) 
        f.truncate()      
    elif int(data)<guessed:
        print(f"High score is {int(data)}")
        print("you need to improve yourself")
    elif int(data)>guessed:
        f.seek(0)
        f.write(str(guessed))
        f.truncate() #f.truncate to clear the past history
        print(f"Now the high score is {int(guessed)}")
        print("you are the high scorer")                
    else:
        print("Draw!")           
print("Thank you for playing")