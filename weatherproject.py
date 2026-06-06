from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


API_KEY = "e949e8679b4bcfbe5da0a0fe3773c941"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

     
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"].title()

        
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        icon_response = requests.get(icon_url)
        icon_image = Image.open(BytesIO(icon_response.content))
        icon_photo = ImageTk.PhotoImage(icon_image)

        weather_icon.config(image=icon_photo)
        weather_icon.image = icon_photo

        
        result_label.config(
            text=f"{description}\n\n"
                 f"Temperature: {temp}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Wind Speed: {wind} m/s"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Weather App")
root.geometry("450x550")
root.config(bg="#87CEEB")


title_label = Label(
    root,
    text="Weather Application",
    font=("Arial", 22, "bold"),
    bg="#87CEEB",
    fg="white"
)
title_label.pack(pady=20)


city_entry = Entry(
    root,
    font=("Arial", 14),
    width=25,
    justify="center"
)
city_entry.pack(pady=10)


search_button = Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    bg="#0077b6",
    fg="white",
    padx=10,
    pady=5,
    command=get_weather
)
search_button.pack(pady=15)


weather_icon = Label(root, bg="#87CEEB")
weather_icon.pack()

result_label = Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#87CEEB",
    fg="white",
    justify="center"
)
result_label.pack(pady=20)

root.mainloop()
