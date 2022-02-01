# Part 1-2
import abc

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return(self.name)
    
    def get_age(self):
        return(self.age)

    def get_marks(self, num):
        marks = []
        for i in range(0,num):
            mark = input("Enter exam mark from 1-100: ")
            while type(mark) != int:
                try:
                    mark = int(mark)
                    if mark < 1 or mark > 100:
                        raise Exception
                    else:
                        continue
                except:
                    mark = input("Please enter an integer value between 1-100: ")
            marks.append(mark)
        return marks
    
    def find_average(self, num=3):
        marks = self.get_marks(num)
        average = round(sum(marks) / len(marks))
        if average >= 65:
            result = "Pass"
        else:
            result = "Fail"
        
        print(f"Average: {average}\nResult: {result}")
        return average, result
    
student1 = Student("Kratos", 50)
student2 = Student("Atreus", 15)

print(student1.get_age())

student1.find_average()


# Part 3

class Bird(abc.ABC):
    def __init__(self):
        self.flightless = False
        self.extant = False

    @abc.abstractmethod
    def is_flightless(self):
        self.flightless = True
    
    @abc.abstractmethod
    def is_extant(self):
        self.extant = True


class Owl(Bird):
    def __init__(self):
        super().__init__()
        super().is_extant()

    def is_flightless(self):
        print("I have the power of flight!")
    
    def is_extant(self):
        print("My species lives on!")

    def get_traits(self):
        return self.flightless, self.extant

class Dodo(Bird):
    def __init__(self):
        super().__init__()
        super().is_flightless()

    def is_flightless(self):
        print("I cannot fly...")
    
    def is_extant(self):
        print("My species is extinct...")

    def get_traits(self):
        return self.flightless, self.extant
        
owl = Owl()
dodo = Dodo()

for animal in (owl, dodo):
    print(animal.get_traits())
    animal.is_flightless()
    animal.is_extant()