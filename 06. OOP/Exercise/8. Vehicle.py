class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.cars = []
        self.owner = None

    def buy(self, money, owner):
        if money >= self.price:
            if self.model not in self.cars:
                self.cars.append(model)
                change = money - self.price
                self.owner = owner
                print(f"Successfully bought a car. Change: {change:.2f}")
            else:
                print("Car already sold")
        else:
            print("Sorry, not enough money")

    def sell(self, ):
        if self.model in self.cars:
            self.owner = None
            self.cars.remove(self.model)
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            print("Vehicle has no owner")

    def __repr__(self):
        if self.owner:
            return f"{model} {self.type} is owned by: {self.owner}"
        else:
            return f"{model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

