from tkinter import *
from opencage.geocoder import OpenCageGeocode


def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            lat = round(results[0]['geometry']["lat"], 3)
            lng = round(results[0]['geometry']["lng"], 3)
            return  f"Широта{lat}, Долгота{lng}"
        else:
            print("Данные не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")


def show_coords(event=None):
    city = entry.get()
    coordinates = get_coords( city, key )
    label.config(text=f"Кординаты города {city}: {coordinates}")


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



window.mainloop()

