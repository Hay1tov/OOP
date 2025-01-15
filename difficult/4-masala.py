from os import system
from colorama import Fore, Style

system('clear')
class Student:
    def __init__(self, name, ball, rating, scholarship):
        self.name = name
        self.ball = ball
        self.rating = rating
        self.scholarship = scholarship

    def sort(self):
        if self.rating == "Grand" and self.ball >= 85:
            print(f"{Style.BRIGHT}{Fore.RED}1 Ism: {Fore.BLUE}{self.name}\n{Fore.RED}2 O`rtacha ball: {Fore.BLUE}{self.ball}\n{Fore.RED}3 Daraja: {Fore.BLUE}{self.rating}\n")
student_list = []
student_list.append(Student("Nurbek", 85, "Grand", 800000))              
student_list.append(Student("Siroj", 90, "Grand", 1200000))              
student_list.append(Student("Sherbek", 70, "kantrakt", 600000))              
student_list.append(Student("Eldor", 189, "Grand", 1800000))              

for student in student_list:
    student.sort()