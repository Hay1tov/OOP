from os import system
from colorama import Fore, Style

system('clear')
class Xodimlar:
    def __init__(self, name, rank, work_time, salary):
        self.name = name
        self.rank = rank
        self.work_time = work_time
        self.salary = salary

    def sort(self):
        if self.work_time > 40 and self.rank == 'Raxbar':
            print(f"{Style.BRIGHT}{Fore.RED}1 Ism: {Fore.BLUE}{self.name}\n{Fore.RED}2 Lavozimi: {Fore.BLUE}{self.rank}\n{Fore.RED}3 Oylik: {Fore.BLUE}{self.salary}\n")
worker_list = []
worker_list.append(Xodimlar("Nurbek", "Raxbar", 46, 15000000))              
worker_list.append(Xodimlar("Sherbek", "sartarosh", 42, 10000000))              
worker_list.append(Xodimlar("Suxrob", "dasturchi", 36, 5000000))              
worker_list.append(Xodimlar("olimjon", "direktor", 50, 18000000))              
worker_list.append(Xodimlar("Asror", "Raxbar", 46, 12000000))                        
for ins in worker_list:
    ins.sort()