from colorama import Fore, Style

class Student:
    def __init__(self, first_name, last_name, course, average_ball):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.average_ball = average_ball

    def name(self):
        return f"{self.first_name} {self.last_name}"

student = Student("Ali", "Valiyev", "English", 50)
print(f"{Fore.GREEN} {Style.BRIGHT}student.name()")