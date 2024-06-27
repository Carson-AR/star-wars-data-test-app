from data import fetch_people
from utilities import find_person


def test_find_luke():
    people = fetch_people()
    person = find_person(people, "luke")
    assert person is not None, "failed to find luke"


def test_find_fred():
    people = fetch_people()
    person = find_person(people, "fred")
    assert person is None, "unexpectedly found fred"
