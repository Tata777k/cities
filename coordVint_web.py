from tkinter import *
from opencage.geocoder import OpenCageGeocode
import webbrowser

def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            lat = results[0]['geometry']["lat"]
            lng = results[0]['geometry']["lng"]

            osm = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            return {"coordinates": f"Широта{lat}, Долгота{lng}",
                    "map_url":osm}
        else:
            return {"coordinates": None",
                    "map_url":None}
    except Exception as e:
        print(f"Ошибка: {e}")
        return {"coordinates": None",
                    "map_url": None}

def show_coords(event=None):
    global map_url
    city = entry.get()
    result = get_coords(city, key)
    map_url = result["map_url"]
    coordinates = result["coordinates"]
    label.config(text=coordinates)


def show_map():
    if map_url:
        webbrowser.open(map_url)


key = '3dd01ff52a054c69a9c49fa7be9d1766'


window = Tk()
window.title("Координаты городов")


entry = Entry()
entry.pack()
entry.bind("<Return>", show_coords)
entry.focus_set()


label = Label(text="Введите город и нажмите кнопку")
label.pack()

but = Button(text="Поиск", command=show_coords)
but.pack()

but_map = Button(text="Открыть карту", command=show_map)
but_map.pack()

window.mainloop()

