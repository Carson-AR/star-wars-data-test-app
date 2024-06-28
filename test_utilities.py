from data import fetch_people
from utilities import find_person
from data import fetch_space_ship
from utilities import find_space_ship


def test_find_luke():
    people = fetch_people()
    person = find_person(people, "luke")
    assert person is not None, "failed to find luke"


def test_find_fred():
    people = fetch_people()
    person = find_person(people, "fred")
    assert person is None, "unexpectedly found fred"


def test_find_death():
    space_ships = find_space_ship()
    space_ship = fetch_space_ship(space_ships, "death")
    assert space_ship is not None, "failed to find death"
