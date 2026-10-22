class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

student1=Student("Prajwal",23)
student1.intro()
student2=Student("Avinash",25)
student2.intro()


from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

student1=Student("Prajwal",23)
student1.intro()