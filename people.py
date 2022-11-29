from datetime import datetime

#generates a string representation of the current timestamp
def get_timestamp() -> str:
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


POEPLE = {
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

def read_all() -> list:
    return list(POEPLE.values())