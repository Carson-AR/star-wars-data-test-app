def find_person(people, persons_name):
    for person in people:
        if persons_name.lower() in person["name"].lower():
            return person

    else:
        print(
            "either we do not have that charactar or you did not enter a valid name. please try again"
        )
