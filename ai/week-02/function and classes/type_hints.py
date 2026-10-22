def add(a:int,b:int)->int:
    return a+b

res=add(1,2)
print(res)

print()

from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age:str

def intro(student:Student)->None:
    print(f"My name is {student.name} and I am {student.age} years old.")


student=Student("Prajwal",23)
intro(student)