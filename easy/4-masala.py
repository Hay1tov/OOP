from colorama import Fore, Style

class Telefon:
    def __init__(self, name, ram, price, company):
        self.name = name
        self.ram = ram
        self.price = price
        self.company = company
    
    def out(self):
        return f"{Fore.GREEN } {Style.BRIGHT} {Style.DIM}Telefon name: {self.name}\nRAM hajmi: {self.ram} GB\nNarxi: {self.price} $\nIshlab chiqaruvchi: {self.company}\n"
    
phone1 = Telefon("iphone 6s", 4, 60, "apple")
phone2 = Telefon("Redmi Note 10 Pro", 6, 190, "xiaomi")
phone3 = Telefon("Apple iPhone 16 Pro", 4, 1200, "apple")
phone4 = Telefon("Samsung s24 Ultra", 8, 1000, "samsung")

phones = [phone1, phone2, phone3, phone4]

for phone in phones:
    if 8 > phone.ram > 2:
        print(phone.out())
