from random import choice
easy_words=["cow","cat","dog","tiger","lion","apple","mango","india"]
medium_words=["monkey","bottle","fridge","orange","laptop","planet"]
hard_words=["elephant","diamond","umbrella","dinosaur","mountain"]
print("Welcome to word guessing game")
print("Choose difficulty level:easy,medium,hard")
level=input("enter difficulty:").lower()
if level=="easy":
    secret=choice(easy_words)
elif level=="medium":
    secret=choice(medium_words)
elif level=="hard":
    secret=choice(hard_words)
attemts=0
print("Guess the word")
while True:
    guess=input("Enter your word:")
    attemts+=1
    if guess==secret:
        print(f"Congratulations you won the game at {attemts} attemts")
        break
    hint=""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint:",hint)
print("Game Over")