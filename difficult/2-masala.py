from os import system
from colorama import Fore, Style

system('clear')
class Instrument:
    def __init__(self, name, price, company, instrument):
        self.name = name
        self.price = price
        self.company = company
        self.instrument = instrument

    def sort(self):
        if self.price > 2000000 and self.instrument == 'klaviatura':
            print(f"{Style.BRIGHT}{Fore.RED}1-instrument-> {Fore.BLUE}{self.name}\n{Fore.RED}2-company-> {Fore.BLUE}{self.company}\n{Fore.RED}3-price-> {Fore.BLUE}{self.price}\n")
list_inst = []  
list_inst.append(Instrument("Piano", 2500000, "Yamaha", "klaviatura"))
list_inst.append(Instrument("Guitar", 1500000, "Fender", "struna"))
list_inst.append(Instrument("Synthesizer", 3000000, "Roland", "klaviatura"))
list_inst.append(Instrument("Violin", 1200000, "Stradivarius", "struna"))
for ins in list_inst:
    ins.sort()