"""change_instance_variable_value"""

class Student:
    """Student class"""
    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def student_details(self):
        """Student details"""
        print(f"name = {self.name}, Age = {self.age}")

student_1 = Student()
student_2 = Student()

student_1.student_details()

student_2.name = "Rajan"
student_2.age = 12

student_2.student_details()
