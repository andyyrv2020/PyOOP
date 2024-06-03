class Car:
    def __init__(self, model, fuel_amount, fuel_consumption):
        self.model = model
        self.fuel_amount = fuel_amount
        self.fuel_consumption = fuel_consumption
        self.distance_traveled = 0

    def drive(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel_amount >= required_fuel:
            self.fuel_amount -= required_fuel
            self.distance_traveled += distance
        else:
            print("Insufficient fuel for the drive")

    def __str__(self):
        return f"{self.model} {self.fuel_amount:.2f} {self.distance_traveled}"

def main():
    n = int(input())
    cars = {}

    for _ in range(n):
        data = input().split()
        model = data[0]
        fuel_amount = float(data[1])
        fuel_consumption = float(data[2])
        cars[model] = Car(model, fuel_amount, fuel_consumption)

    while True:
        command = input()
        if command == "End":
            break
        command_parts = command.split()
        if command_parts[0] == "Drive":
            model = command_parts[1]
            distance = int(command_parts[2])
            if model in cars:
                cars[model].drive(distance)

    for car in cars.values():
        print(car)

if __name__ == "__main__":
    main()
