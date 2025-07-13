def temperature():
    convert_temp=int(input("What do you want to convert?\n1.Celsius to fahrenheit\n2.Fahrenheit to Celsius\n"))
    if convert_temp==1:
        temp_1=float(input("Enter the temperature in Celsius: "))
        fahrenheit_temp=(temp_1*9/5)+32
        print(f"Fahrenheit temperature is {fahrenheit_temp}°F")
    elif convert_temp==2:
        temp_2=float(input("Enter the temperature in Fahrenheit: "))
        celsius_temp=(temp_2-32)*5/9
        print(f"Celsius temperature is {celsius_temp}°C")
    else:
        print("Invalid Input (Choose from options)")
def weight():
    convert_weight=int(input("What do you want to convert?\n1.gram to kilogram\n2.kilogram to gram\n3.kilogram to pound(lb)\n4.gram to pound(lb)\n5.pound to gram\n6.pound to kilogram\n"))
    if convert_weight==1:
        gram=float(input("Enter weight in gram: "))
        kilogram=gram/1000
        print(f"weight in kilogram is {kilogram:.2f} kg")
    elif convert_weight==2:
        kilogram_input=float(input("Enter weight in kilogram: "))
        gram_output=kilogram_input*1000
        print(f"weight in gram is {gram_output:.2f} g")
    elif convert_weight==3:
        kilogram_to_pound=float(input("Enter weight in kilogram: "))
        pound=kilogram_to_pound*2.20462
        print(f"weight in pound(lb) is {pound} lb")
    elif convert_weight==4:
        gram_input=float(input("Enter weight in gram: "))
        pound_output=gram_input*0.00220462
        print(f"weight in pound is {pound_output} lb")
    elif convert_weight==5:
        pound_input=float(input("Enter weight in pound: "))
        pound_gram=pound_input*453.592
        print(f"weight in gram is {pound_gram} g")
    elif convert_weight==6:
        pound_kg=float(input("Enter weight in pound: "))
        pound_kilogram=pound_kg*0.453592
        print(f"weight in kilogram is {pound_kilogram} kg")
    else:
        print("Invalid input!(choose from the options)")
def length():
    print("What do you want to convert?")
    print("1.kilometre to metre")
    print("2.kilometre to centimetre")
    print("3.kilometre to foot")
    print("4.metre to kilometre")
    print("5.metre to centimetre")
    print("6.metre to foot")
    print("7.centimetre to kilometre")
    print("8.centimetre to metre")
    print("9.centimetre to foot")
    print("10.foot to kilometre")
    print("11.foot to metre")
    print("12.foot to centimetre")
    length=int(input())
    if length==1:
        km_1=float(input("Enter length in km: "))
        m_1=km_1*1000
        print(f"length in metre is {m_1} m")
    elif length==2:
        km_2=float(input("Enter length in km: "))
        cm_1=km_2*100000
        print(f"length in centimetre is {cm_1} cm")
    elif length==3:
        km_3=float(input("Enter length in km: "))
        f_1=km_3*3280.84
        print(f"length in foot is {f_1} ft")
    elif length==4:
        m_2=float(input("Enter length in m: "))
        km=m_2/1000
        print(f"length in kilometre is {km} km")
    elif length==5:
        m_3=float(input("Enter length in m: "))
        cm=m_3*100
        print(f"length in centimetre is {cm} cm")
    elif length==6:
        m_4=float(input("Enter length in m: "))
        ft=m_4* 3.28084
        print(f"length in foot is {ft} ft")
    elif length==7:
        cm_2=float(input("Enter length in cm: "))
        km_4=cm_2/100000
        print(f"length in kilometre is {km_4} km")
    elif length==8:
        cm_3=float(input("Enter length in cm: "))
        m_5=cm_3/100
        print(f"length in metre is {m_5} m")
    elif length==9:
        cm_4=float(input("Enter length in cm: "))
        f_2=cm_4*0.0328084
        print(f"length in foot is {f_2} ft")
    elif length==10:
        f_3=float(input("Enter length in foot: "))
        km_5=f_3*0.0003048
        print(f"length in kilometre is {km_5} km")
    elif length==11:
        f_4=float(input("Enter length in foot: "))
        m_1=f_4*0.3048
        print(f"length in metre is {m_1} m")
    elif length==12:
        f_6=float(input("Enter length in foot: "))
        cm_5=f_6*30.48
        print(f"length in centimetre is {cm_5} cm")
    else:
        print("Invalid input!")
        print("Choose from the options")
def main():
    print("_______Welcome to unit converter_______")
    converter=input("Choose what will you want to convert\na.length\nb.weight\nc.temperature\n")
    if converter.lower()=="a":
        length()
    elif converter=="b":
        weight()
    elif converter=="c":
        temperature()
    else:
        print("Invalid Choice!")
        print("Choose from options") 
        
while True:
    try:
        start_programme=input("Do you want to start the programme?(Y/N)\n")
        if start_programme.lower()=="y":
            main()
        elif start_programme.lower()=="n":
            print("Thanks for coming")
            print("closing the programme...")
            break
        else:
            print("invalid input!")
            print("enter Y or N")
    except ValueError:
        print("Choose Y or N")


    

    



        
        
    