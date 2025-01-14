from colorama import Fore, Style
from os import system

system('clear')

class Student:
    def __init__(self, name, course, avarage_ball, scholarship):
        self.name = name
        self.course = course
        self.avarage_ball = avarage_ball
        self.scholarship = scholarship

    def sort(self):
        if self.avarage_ball > 80 and self.scholarship > 1_000_000:
            print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}name-> {Fore.BLUE}{self.name}{Fore.LIGHTWHITE_EX}\ncourse-> {Fore.BLUE}{self.course}{Fore.LIGHTWHITE_EX}\navarage grade-> {Fore.BLUE}{self.avarage_ball}")


student_list = []
student_list.append(Student("Nurbek", 1, 81, 550000))
student_list.append(Student("Sherbek", 1, 70, 800000))
student_list.append(Student("Suxrob", 3, 90, 1200000))
student_list.append(Student("Eldor", 4, 100, 2000000))

for student in student_list:
    student.sort()