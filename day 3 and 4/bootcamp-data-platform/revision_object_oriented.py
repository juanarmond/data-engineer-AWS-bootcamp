# Object Oriented Review.

class Person:
    def __init__(self, firstname, lastname, years):
        self.firstname = firstname
        self.lastname = lastname
        self.years = years

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.years} old."


class Dog:
    def __init__(self, name, breed, years):
        self.name = name
        self.breed = breed
        self.years = years

    def __str__(self):
        return f"{self.name} is {self.breed} and is {self.years} old."

    def is_dog(self):
        return True


class DataEngineer(Person):
    def __init__(self,firstname, lastname, years, experience):
        super().__init__(firstname, lastname, years)
        self.experience = experience

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.years} old, "\
        f"is Data Engineer and has {self.experience} years of experience."


juan = Person(firstname='Juan', lastname='Armond', years=39)
print(juan)


belisco = Dog(name='Belisco', breed='Lhasa', years=1.9)
print(belisco)
print(belisco.is_dog())

juan = DataEngineer(firstname='Juan', lastname='Armond', years=39, experience=2)
print(juan)
