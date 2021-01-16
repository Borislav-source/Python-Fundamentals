class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.value = capacity

    def add_item(self, item):
        if self.value:
            self.items.append(item)
            self.value -= 1
        else:
            print("not enough room in the inventory")

    def get_capacity(self,):
        return self.__capacity

    def __repr__(self):
        result = ", ".join(self.items)
        return f"Items: {result}.\nCapacity left: {self.value}"


inv = Inventory(2)
inv.add_item("potion")
inv.add_item("sword")
inv.add_item("bottle")
print(inv.get_capacity())
print(inv)
