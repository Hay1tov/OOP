from colorama import Fore, Style

class car:
    def __init__(self, marka: str, model: str, year: int, price: int):
        self.marka = marka
        self.model = model
        self.year = year
        self.price = price
    def produced(self):
        if self.year > 2010:
            print(f"{Fore.RED} {Style.BRIGHT}{self.marka}, {self.model}, yili {self.year}   price {self.price}$")
collection = []
car1 = car('Chevrolit', 'Nexia 3', 2018, 10000)
car2 = car('Chevrorit', 'Gentra', 2013, 11000)
car3 = car('Chevrolit', 'Nexia 1', 2002, 6000)

collection.append(car1)
collection.append(car2)
collection.append(car3)

for car in collection:
    car.produced()