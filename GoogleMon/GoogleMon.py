class Company:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = float(salary)

    def __str__(self):
        return f"Company: {self.name}\nDepartment: {self.department}\nSalary: {self.salary:.2f}"

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f"Pokemon: {self.name} {self.type}"

class Parent:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return f"Parent: {self.name} {self.birthdate}"

class Child:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return f"Child: {self.name} {self.birthdate}"

class Car:
    def __init__(self, model, speed):
        self.model = model
        self.speed = int(speed)

    def __str__(self):
        return f"Car: {self.model} {self.speed}"

class Person:
    def __init__(self, name):
        self.name = name
        self.company = None
        self.car = None
        self.pokemons = []
        self.parents = []
        self.children = []

    def set_company(self, company):
        self.company = company

    def set_car(self, car):
        self.car = car

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        result = f"{self.name}\n"
        if self.company:
            result += f"{self.company}\n"
        if self.car:
            result += f"{self.car}\n"
        for pokemon in self.pokemons:
            result += f"{pokemon}\n"
        for parent in self.parents:
            result += f"{parent}\n"
        for child in self.children:
            result += f"{child}\n"
        return result.strip()

def main():
    people = {}

    while True:
        command = input()
        if command == "End":
            break
        parts = command.split()
        name = parts[0]
        if name not in people:
            people[name] = Person(name)
        if parts[1] == "company":
            company = Company(parts[2], parts[3], parts[4])
            people[name].set_company(company)
        elif parts[1] == "pokemon":
            pokemon = Pokemon(parts[2], parts[3])
            people[name].add_pokemon(pokemon)
        elif parts[1] == "parents":
            parent = Parent(parts[2], parts[3])
            people[name].add_parent(parent)
        elif parts[1] == "children":
            child = Child(parts[2], parts[3])
            people[name].add_child(child)
        elif parts[1] == "car":
            car = Car(parts[2], parts[3])
