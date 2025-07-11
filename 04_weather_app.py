import requests
def get_weather(city,api_key):
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city, #q is the correct key for city name
        "appid":api_key, #api id should be written as appid
        "units":"metric"
    }
    response=requests.get(base_url,params=params)
    data=response.json()
    if(response.status_code==200):
        print(f"City name:{data['name'],data['sys']['country']}")
        print(f"Temparature:{data['main']['temp']}")
        print(f"weather:{data['weather'][0]['description']}")
        print(f"Humidity:{data['main']['humidity']}")
    else:
        print("This is not available")
api_key="f31e45e2bf5ace15855c80badf764d04"
city=input("Enter your city name: ")
get_weather(city,api_key)
while True:
    ask=input("Do you want to know another weather conditioin of any location?(Y/N): ")
    if ask.lower()=="y":
        repeat_city=input("Enter your city name: ")
        get_weather(repeat_city,api_key)
    elif ask=="n":
        print("Thanks for using this weather app....")
        print("Thank you")
        print("closing the programm....")
        break
    else:
        print("Invalid input")