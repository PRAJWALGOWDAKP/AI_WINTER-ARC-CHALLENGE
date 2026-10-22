from dataclasses import dataclass
@dataclass
class Student:
    name:str
    marks:list[int]

def total(*marks:int)->int:
    return sum(marks)

def create_student(name:str,**kwargs)->Student:
    marks=kwargs.get("marks",[])
    return Student(name=name,marks=marks)

def student_report(student:Student)->None:
    total_marks=total(*student.marks)
    print(f"Student Name: {student.name}")
    print(f"Marks: {student.marks}")
    print(f"Total Marks: {total_marks}")

student=create_student("Prajwal", marks=[90,80,70])
student_report(student)
