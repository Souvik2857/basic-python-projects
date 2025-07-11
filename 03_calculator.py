def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    if (a==0 or b==0):
        print("You have entered Zero which is not divisible in python")
    else:
        return a/b
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
choice=input("What you want to do?\na.Add\nb.Divide\nc.Multyplication\nd.Subtraction\n")
if choice.lower()=="a":
    print(f"the sum of {num1} and {num2} is {sum(num1,num2)}")
    with open ("D:\\Documents\\Programming\\Home project\\history.txt","a") as f:
        f.write(f"{num1}+{num2}={num1+num2}\n")        
elif choice.lower()=="b":
    print(f"the Division of {num1} by {num2} is {div(num1,num2)}")
    with open ("D:\\Documents\\Programming\\Home project\\history.txt","a") as f:
        f.write(f"{num1}/{num2}={num1/num2}\n")        
elif choice.lower()=="c":
    print(f"the multyplication of {num1} and {num2} is {mul(num1,num2)}")
    with open ("D:\\Documents\\Programming\\Home project\\history.txt","a") as f:
        f.write(f"{num1}X{num2}={num1*num2}\n")        
elif choice.lower()=="d":
     print(f"the Subtrsction of {num1} and {num2} is {sub(num1,num2)}")
     with open ("D:\\Documents\\Programming\\Home project\\history.txt","a") as f:
        f.write(f"{num1}-{num2}={num1-num2}\n")        
else:
    print("Condition not met Succesfully")
    
