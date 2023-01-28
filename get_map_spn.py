def get_map_spn(address: str, long_lat: tuple) -> tuple[float, float]:
    is_valid_spn = False
    while not is_valid_spn:
        print("Введите протяжённость области показа карты по долготе и широте")
        print("Ваш адрес", address)
        print("Ваш центр координат", long_lat)
        try:
            longitude = float(input("Введите градусы долготы > "))
            latitude = float(input("Введите градусы широты > "))
            if 0 <= longitude <= 180 and 0 <= latitude <= 90:
                return longitude, latitude
            else:
                raise Exception("Неверные данные об области показа (lon=(-180, 180), lat=(-90, 90))",
                                longitude, latitude)
        except Exception as e:
            print(e)
            continue
