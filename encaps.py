class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


person = Person('Dev', 30)
person.display()

print(person.name)
print(person.age)