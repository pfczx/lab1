class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom – adres: {self.address}, "
            f"powierzchnia: {self.area} m2, "
            f"działka: {self.plot} m2, "
            f"pokoje: {self.rooms}, "
            f"cena: {self.price} zł")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie – adres: {self.address}, "
            f"powierzchnia: {self.area} m2, "
            f"piętro: {self.floor}, "
            f"pokoje: {self.rooms}, "
            f"cena: {self.price} zł")


d = House(area=120, rooms=5, price=750000,
          address="ul. Lipowa 10, Kraków", plot=400,)

m = Flat(area=55, rooms=2, price=420000,
         address="ul. Rajska 3/12, Kraków", floor=4,)

print(d)
print(m)
