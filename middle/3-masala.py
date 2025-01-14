from colorama import Fore, Style
from os import system

system('clear')

class Student:
    grades = []
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ball(self, science_ball):
        self.grades.append(science_ball)

    def get_average(self)->float:
        self.avarage = sum(self.grades)/len(self.grades)
        return self.avarage
    
    def is_passing(self):
        if self.get_average() > 60:
            return 'True'
        else:
            return 'False'

student = Student("Eldor", 19)

student.ball(90)
student.ball(100)
student.ball(80)

urtacha_ball = student.get_average()
print(f"{Fore.RED}{Style.BRIGHT}---{student.name}ning o`rtacha ball:{Fore.RESET} {Fore.YELLOW}{urtacha_ball} {Fore.RED}va bu  -->: {Fore.RESET}{Fore.YELLOW}{student.is_passing()}")




        