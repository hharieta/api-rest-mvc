from datetime import datetime
from flask import abort, make_response

#generates a string representation of the current timestamp
def get_timestamp() -> str:
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

# /people GET
def read_all() -> list:
    return list(PEOPLE.values())


# /people/{lname} GET
def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f'Person with last name {lname} not found'
        )


# /people POST
def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and fname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f'Person with last name {lname} already exists',
        )

# /people/{lname} PUT
def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]
    else:
        abort(
            404,
            f'Person with last name {lname} not found'
        )


# /people/{lname} DELETE
def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f'{lname} succesfully deleted', 200
        )
    else:
        abort(
            404,
            f'Person with last name {lname} not found'
        )