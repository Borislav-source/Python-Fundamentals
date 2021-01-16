class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def animal_count(self, total_count):
        self.__animals = total_count

    def get_info(self, info):
        if info == "mammal":
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}")
        elif info == "fish":
            print(f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}")
        elif info == "bird":
            print(f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}")


zoo = Zoo(input())
total_count = int(input())
zoo.animal_count(total_count)
for animal in range(total_count):
    data = input()
    species, name = list(data.split())
    zoo.add_animal(species, name)
info = input()
zoo.get_info(info)
