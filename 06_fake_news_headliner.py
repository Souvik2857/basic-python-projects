import random
while True:
    subject=["Sharukh Khan","Tiger Shroff","Salman","Mamata","Modi"]
    sub=random.choice(subject)
    verb=["is eating","is dancicg on","is riding on","is sleeping on ","is declare war against"]
    ver=random.choice(verb)
    obj=["Crows","red fort","Buffalo","Pakistan","Mumbai street"]
    o=random.choice(obj)
    print(f"{sub} {ver} {o}")
    repeat=input(f"Do you want to get more fake news?\n(yes or no)\n").strip().lower()
    
    if(repeat=="no"):
        print("Thanks for playing")
        break
    
print("we are closing the programme.....")
        

