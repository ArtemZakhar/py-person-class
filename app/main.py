class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_persons = [Person(person["name"], person["age"]) for person in people]

    for index, new_person in enumerate(new_persons):
        person_data = people[index]
        if person_data.get("wife"):
            new_person.wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            new_person.husband = Person.people[person_data["husband"]]

    return new_persons
