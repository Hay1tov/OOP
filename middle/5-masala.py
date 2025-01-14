from os import system
from colorama import Fore, Style

system('clear')

class ShoppingCart:
    def __init__(self, item=None, price=0) -> None:
        self.item = item
        self.price = price
    
    def add_item(self):
        self.item = input(f"{Fore.RED}{Style.BRIGHT}\nmahsulotni tanlang: ")
        self.price = int(input(f"{Fore.RED}{Style.BRIGHT}narxi qancha: "))
        products.append(self)
    
    def remove_item(self):
        self.item = input(f"{Fore.RED}{Style.BRIGHT}O'chirmoqchi bo'lgan mahsulotinngz nomi nima: ")
        if self.item in products:
            products.remove(self.item)
            print(f"{Fore.BLUE}{Style.BRIGHT}O'chirildi")
        else:
            print(f"{Fore.BLUE}{Style.BRIGHT}Topilmadi")
                
    
    def get_total(self):
        total = 0
        for product in products:
            total += product.price
        
        return total
            
product1 = ShoppingCart("olma", 10000)
product2 = ShoppingCart("kartoshka", 8000)
product3 = ShoppingCart("qo'y go'sht", 110000)
product4 = ShoppingCart("piyoz", 4000)
products = [product1, product2, product3, product4]

n = 0
while n != 4:
    print(f"{Fore.GREEN}{Style.BRIGHT}\nxarid qilish - 1", "mahsulotni o'chirish - 2", "jami mahsulotni hisoblash - 3", "exit - 4", sep="\n")
    
    n = int(input(f"{Fore.RED}{Style.BRIGHT}buyruqni tanlang: "))
    
    if n == 1:
        r = int(input(f"{Fore.YELLOW}{Style.BRIGHT}\nqancha mahsulot qo'chmoqchisiz: "))
        for i in range(r):
            cart = ShoppingCart()
            cart.add_item()
    
    if n == 2:
        product_num = int(input(f"{Fore.YELLOW}{Style.BRIGHT}qancha mahsulotni o'chirmoqchisiz: "))
        for i in range(product_num):
            remove = ShoppingCart()
            remove.remove_item()
            
    if n == 3:
        product = ShoppingCart()
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\njami narx: {product.get_total()}")
        