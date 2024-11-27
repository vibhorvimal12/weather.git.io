from tkinter import *
from tkinter import messagebox
import requests

def tell_weather():
    api_key = "3e8d873f6a66da43f01f03d9ed7c8080" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()

    if not city_name.strip():
        messagebox.showerror("Error", "City name cannot be empty!")
        return

    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  
        x = response.json()

        if x.get("cod") != 200:
            messagebox.showerror("Error", f"Error: {x.get('message', 'Unknown error')}")
            city_field.delete(0, END)
            return

        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        temp_field.insert(15, f"{current_temperature} Kelvin")
        atm_field.insert(10, f"{current_pressure} hPa")
        humid_field.insert(15, f"{current_humidity} %")
        desc_field.insert(10, weather_description)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error: {e}")
    except KeyError:
        messagebox.showerror("Error", "Unexpected response from API. Please try again.")

def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    city_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.title("Weather Application")
    root.configure(background="light blue")
    root.geometry("425x225")

    
    headlabel = Label(root, text="Weather GUI Application", fg='white', bg='black')
    label1 = Label(root, text="City name:", fg='white', bg='dark gray')
    label2 = Label(root, text="Temperature:", fg='white', bg='dark gray')
    label3 = Label(root, text="Atmospheric pressure:", fg='white', bg='dark gray')
    label4 = Label(root, text="Humidity:", fg='white', bg='dark gray')
    label5 = Label(root, text="Description:", fg='white', bg='dark gray')

   
    headlabel.grid(row=0, column=1, pady=10)
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=3, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    label4.grid(row=5, column=0, sticky="E")
    label5.grid(row=6, column=0, sticky="E")

 
    city_field = Entry(root)
    temp_field = Entry(root)
    atm_field = Entry(root)
    humid_field = Entry(root)
    desc_field = Entry(root)

    city_field.grid(row=1, column=1, ipadx="100")
    temp_field.grid(row=3, column=1, ipadx="100")
    atm_field.grid(row=4, column=1, ipadx="100")
    humid_field.grid(row=5, column=1, ipadx="100")
    desc_field.grid(row=6, column=1, ipadx="100")

    
    button1 = Button(root, text="Submit", bg="pink", fg="black", command=tell_weather)
    button2 = Button(root, text="Clear", bg="pink", fg="black", command=clear_all)

    button1.grid(row=2, column=1, pady=10)
    button2.grid(row=7, column=1, pady=10)

   
    root.mainloop()
