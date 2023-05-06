import datetime

today = datetime.date.today().year

class Student:
    # school ="AKirachix"
    def __init__(self,first_name,last_name,age,country):
        
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def show_full_name(self):
            return f"{self.first_name} {self.last_name}" 
    def year_of_birth(self):
        year=2023-self.age
        return f" hello {self.first_name},you were born in {year}"

    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"

stud = Student("Ann","Akech",20,"South SUdan")
print(stud.show_full_name())
print(stud.year_of_birth())
print(stud.initials())
   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("John", 25)
person1.greet()

      


    