def show_history():
    with open("D:\\Documents\\Programming\\Home project\\advanced_calculator.txt") as f:
        read=f.read()
        if(read==""):
            print("No history found")
        else:
            print(read)
def clear_history():
    with open("D:\\Documents\\Programming\\Home project\\advanced_calculator.txt","w") as f:
        f.write("")
        print("History cleared")
def save_history(equation,result):
    with open("D:\\Documents\\Programming\\Home project\\advanced_calculator.txt","a") as f:
        f.write(equation+"="+str(result)+"\n")
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("invalid input")
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if (num2==0):
            print("This equation can't divided by Zero")
            return
        result=num1/num2
    else:
        print("Invalid operator")
        return
    if int(result)==result:
        result=int(result)
    print(f"result: {result}")
    save_history(user_input,result)
def main():
    print("___WELCOME TO SIMPLE CALCULATOR___")
    while True:
        user_input=input("Enter your calculation or command (history,clear,exit)\n").lower()
        if user_input.lower()=="history":
            show_history()
        elif user_input.lower()=="clear":
            clear_history()
        elif user_input.lower()=="exit":
            print("Goodbye......")
            break
        else:
            calculate(user_input)
    
main()
        

