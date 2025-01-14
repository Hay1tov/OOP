from colorama import Fore, Style
class Restaurant:
    def __init__(self):
        pass
    
class FastFood(Restaurant):
    def __init__(self, food , price):
        self.food = food
        self.price = price
        
    def Menu_fastFood(self):
        return f"{Style.RESET_ALL}{Fore.CYAN}{self.food} {Fore.GREEN}{self.price}{Style.RESET_ALL}"
    
class FineDining(Restaurant):
    def __init__(self, food, price):
        self.food = food
        self.price = price
    
    def Menu_fineDining(self):
        return f"{Style.RESET_ALL}{Fore.CYAN}{self.food}{Style.RESET_ALL}  {Fore.GREEN}{self.price}"
        

fastfood1 = FastFood("Hot-dog", 15000) 
fastfood2 = FastFood("Lavash", 35000) 
fastfood3 = FastFood("Burger", 35000) 
FastFoods = [fastfood1, fastfood2, fastfood3]


finedining1 = FineDining("Manti",  10000)
finedining2 = FineDining("osh",  40000)
finedining3 = FineDining("Yaxna",  190000)
finedining4 = FineDining("Sho'rva", 8000)
FineDinings = [finedining1, finedining2, finedining3, finedining4]

print(f"\n{Fore.MAGENTA}Restaurant: {Fore.WHITE}FineDining")
print(f"{Fore.BLUE} {Style.BRIGHT}Food    {Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}Prices")
for food in FineDinings:
    print(food.Menu_fineDining())
    
print(f"\n{Fore.MAGENTA}Restauratn: {Fore.WHITE}FastFood")
print(f"{Fore.BLUE} {Style.BRIGHT}Food    {Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}Prices")
for fastfood in FastFoods:
    print(fastfood.Menu_fastFood())