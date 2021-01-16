class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite_people(self, name):
        self.people.append(name)

    def people_count(self):
        return len(self.people)

    def party_names(self):
        return ", ".join([person.name for person in self.people])


party = Party()
while True:
    command = input()
    if command == 'End':
        break

    name = command
    person = Person(name)
    party.invite_people(person)

print(f"Going: {party.party_names()}")
print(f"Total: {party.people_count()}")
