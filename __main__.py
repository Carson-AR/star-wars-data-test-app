from data import fetch_people
from utilities import find_person
from data import fetch_space_ships
from utilities import find_space_ship

name = input("what person or ship would you like")
# question()
people = fetch_people()
person = find_person(people, name)
if person is not None:
    print(person)
else:
    space_ships = fetch_space_ships()
    space_ship = find_space_ship(space_ships, name)
    print(space_ship)

#
