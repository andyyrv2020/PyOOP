class Engine:
    def __init__(self, model, power, displacement="n/a", efficiency="n/a"):
        self.model = model
        self.power = power
        self.displacement = displacement
        self.efficiency = efficiency

    def __str__(self):
        return f"  {self.model}:\n    Power: {self.power}\n    Displacement: {self.displacement}\n    Efficiency: {self.efficiency}"

class Car:
    def __init__(self, model, engine, weight="n/a", color="n/a"):
        self.model = model
        self.engine = engine
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"{self.model}:\n{self.engine}\n  Weight: {self.weight}\n  Color: {self.color}"

def main():
    n = int(input())
    engines = {}

    for _ in range(n):
        data = input().split()
        model = data[0]
        power = int(data[1])
        displacement = data[2] if len(data) > 2 else "n/a"
        efficiency = data[3] if len(data) > 3 else "n/a"
        engines[model] = Engine(model, power, displacement, efficiency)

    m = int(input())
    cars = []

    for _ in range(m):
        data = input().split()
        model = data[0]
        engine_model = data[1]
        weight = data[2] if len(data) > 2 else "n/a"
        color = data[3] if len(data) > 3 else "n/a"
        car = Car(model, engines[engine_model], weight, color)
        cars.append(car)

    for car in cars:
        print(car)

if __name__ == "__main__":
    main()

