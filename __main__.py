from questoin import question
from data import fetch_people
from utilities import find_person
from data import fetch_space_ship
from utilities import find_space_ship
from questoin import ship_question

name = input("what person or ship would you like")
# question()
people = fetch_people()
person = find_person(people, name)
if person is not None:
    print(person)
else:
    space_ships = fetch_space_ship()
    space_ship = find_space_ship(space_ships, name)
    print(space_ship)

#
