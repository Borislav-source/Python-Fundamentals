number_of_cars = int(input())
cars_dict = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars_dict[car] = [int(mileage), int(fuel)]

data = input()

while not data == 'Stop':
    data = data.split(' : ')
    command, car = data[:2]
    if command == 'Drive':
        distance, fuel = [int(i) for i in data[2:]]
        if fuel <= cars_dict[car][1]:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars_dict[car][0] >= 100000:
            del cars_dict[car]
            print(f"Time to sell the {car}!")
    elif command == 'Refuel':
        fuel = int(data[2])
        if fuel + cars_dict[car][1] <= 75:
            cars_dict[car][1] += fuel
        else:
            fuel -= (cars_dict[car][1] + fuel) - 75
            cars_dict[car][1] = 75
        print(f"{car} refueled with {fuel} liters")
    elif command == 'Revert':
        kilometers = int(data[2])
        if cars_dict[car][0] - kilometers >= 10000:
            cars_dict[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars_dict[car][0] = 10000
    data = input()

for key in dict(sorted(cars_dict.items(), key= lambda x: (-x[1][0], x[0]))):
    print(f"{key} -> Mileage: {cars_dict[key][0]} kms, Fuel in the tank: {cars_dict[key][1]} lt.")
