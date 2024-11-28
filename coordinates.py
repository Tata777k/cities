from opencage.geocoder import OpenCageGeocode


def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            lat = round(results[0][geometry]["lat"], 3)
            lng = round(results[0][geometry]["lng"], 3)
            return  f"Широта{lat}, Долгота{lng}"
        else:
            print("Данные не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")

key = '3dd01ff52a054c69a9c49fa7be9d1766'
city = "Уфа"

coordinates = get_coords(city, key)

if coordinates:
    print(f"Кординаты города {city}: {coordinates}")

# query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'

