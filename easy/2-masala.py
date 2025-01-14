from colorama import Fore, Style

class Employe:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def Salary(self):
        return f"{self.salary}"

staff = Employe("Ali", 100)

print(f"{Fore.GREEN} {Style.BRIGHT}Xodimning yillik maoshi -> {staff.salary*12}")