from questoin import question
from data import fetch_people
from utilities import find_person


whos_data = " "


# question()
people = fetch_people()
persons_name = input(
    "whos data would you like to see? (with no spaces between words, no caps)"
)
person = find_person(people, persons_name)
print(person)
