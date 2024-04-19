import requests
from tkinter import *
import math

city_name="Hyderabad,India"
api_key="5ae40699b4dcf4d9e8cf71a26a102cc9"

def get_weather(api_key,city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response=requests.get(url).json()
    temp = response['main']['temp']
    #temp = math.floor((temp * 1.8) - 459.67)   converts to F
    temp=math.floor(temp-273.15) #coverting to celcius
    feels_like=response['main']['feels_like']
    feels_like = math.floor(feels_like-273.15)
    humidity=response['main']['humidity']


    #print(temp)
    #print(feels_like)
    #print(humidity)

    return{
        'temp':temp,
        'feels_like':feels_like,
        'humidity':humidity
    }

weather= get_weather(api_key,city_name)

print(weather['temp'])
print(weather['feels_like'])
print(weather['humidity'])


root= Tk()
root.geometry("500x500")
root.title(f'{city_name[:]} Weather')

def display_city_name(city):
    city_label=Label(root,text=f"{city_name[:-6]}")
    city_label.config(font=("Comic Sans MS",35))
    city_label.pack(side='top')

def display_stats(weather):
    temp = Label(root, text=f"Temperature: {weather['temp']}°C")
    feels_like = Label(root, text=f"Feels Like: {weather['feels_like']}°C")
    humidity = Label(root, text=f"Humidity: {weather['humidity']} %")

    temp.config(font=("Comic Sans MS", 22))
    feels_like.config(font=("Comic Sans MS", 19))
    humidity.config(font=("Comic Sans MS", 19))

    temp.pack(side="top")
    feels_like.pack(side="top")
    humidity.pack(side="top")


display_city_name(city_name)
display_stats(weather)


mainloop()
