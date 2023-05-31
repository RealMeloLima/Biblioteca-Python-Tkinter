import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


def getWeather(city):
    API_key = '7407ebf0516cde0fc45fe2d132bcb473'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror('Error', 'City not found')
        return None
    

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


def search():
    city = cityEntry.get()
    result = getWeather(city)
    if result is None:
        return
    
    icon_url, temperature, description, city, country = result
    locationLabel.config(text= f'{city}, {country}')

    image = Image.open(requests.get(icon_url, stream= True).raw)
    icon = ImageTk.PhotoImage(image)
    iconLabel.config(image=icon)
    iconLabel.image = icon

    tempLabel.config(text=f'Temperature: {temperature:.2f}°C')
    descLabel.config(text= f'Description: {description}')


window = ttkbootstrap.Window(themename= 'darkly')
window.title('Weather App')
window.geometry('400x400')


cityEntry = ttkbootstrap.Entry(window, font= 'Helvetica, 18')
cityEntry.pack(pady=10)


searchButton = ttkbootstrap.Button(window, text= 'Search', command= search, bootstyle= 'warning')
searchButton.pack(pady=10)

locationLabel = tk.Label(window, font= 'Helvetica, 25')
locationLabel.pack(pady=20)


iconLabel = tk.Label(window)
iconLabel.pack()


tempLabel = tk.Label(window, font='Helvetica, 20')
tempLabel.pack()


descLabel = tk.Label(window, font='Helvetica, 20')
descLabel.pack()

window.mainloop()