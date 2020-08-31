from dataclasses import dataclass

@dataclass
class Student:
    name:str
    starID: str
    GPA: float

    


def main():
    abdala  = Student('Abdala', 'qi4833yf', 3.21)
    print(abdala)
    print(abdala.GPA)
    print(abdala.name)
    print(abdala.starID)
    
main()

