from colorama import Style, Fore

class School:
    
    def __init__(self):

        self.school = []

    def add_student(self):

        student_name = input(f"{Fore.BLUE} Talabaning ismini kiriting: ")
        student_Lname = input(f"{Fore.BLUE} Talabaning familyasini kiriting: ")

        try:

            student_phone = int(input(f"{Fore.BLUE} Telefon raqamni kiriting: "))

        except ValueError:

            print(f"{Fore.RED} {Style.DIM}  Error! ")
            return

        self.school.append({"student_name": student_name, "student_Lname": student_Lname, "student_phone": student_phone})

        print(f"{Style.BRIGHT} {Fore.RED} {student_name} muvaffaqiyatli qo'shildi! {Fore.RESET}")

    def delete_student(self):

        dell = input(f"{Fore.BLACK} O'quvchining ismini kiriting: ")

        for student in self.school:

            if student["student_name"] == dell:

                self.school.remove(student)
                print(f"{Style.BRIGHT} {Fore.RED} Talaba muvaffaqiyatli o'chirildi ")
                return
                
        print(f"{Style.DIM} {Fore.RED} Talaba topilmadi {Style.RESET_ALL}")

pupil = School()
pupil.add_student()
pupil.delete_student()
