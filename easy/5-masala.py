from colorama import Fore, Style

class Market:
    def __init__(self, market: str, manzil: str, mahsulot: str, ish_vaqti: int):
        self.market = market
        self.manzil = manzil
        self.mahsulot = mahsulot
        self.ish_vaqti = ish_vaqti
    def list(self):
        if self.mahsulot == "Electronic":
            print(f"\n{Fore.RED} {Style.BRIGHT}do'kon-> {self.market}\n manzil-> {self.manzil}\n mahsulot turi-> {self.mahsulot}\n ish vaqti-> {self.ish_vaqti}")

market1 = Market("Briliant Market", "Registon", "Electronic", "08:00 to 20:00")
market2 = Market("Akfa", "Rudakiy", "door and window", "10:00 to 22:00")
market3 = Market("Phones", "Ibn Sino street", "only iphones", "06:00 to 18:00")

market1.list()
market2.list()
market3.list()