# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/1/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------


import random
import json
from typing import List

# -----------------------Inventory Manage Dataset-----------------------

def generate_random_inventory(count: int = 100, seed: int = 42) -> List[int]:
    random.seed(seed)
    return random.sample(range(1000, 9999), count)

def save_to_file(data: List[int], filename: str = "inventory_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_from_file(filename: str = "inventory_data.json") -> List[int]:
    with open(filename, 'r') as f:
        return json.load(f)

# -----------------------Airline Flight Manage Dataset-----------------------
AIRLINE_CODES = ["AA", "BA", "DL", "UA", "SW", "AF", "LH", "EK"]

def generate_flight_numbers(count: int = 50, seed: int = 99) -> List[str]:
    random.seed(seed)
    flights = set()
    while len(flights) < count:
        code = random.choice(AIRLINE_CODES)
        number = random.randint(100, 999)
        flights.add(f"{code}{number}")
    return list(flights)

def save_to_file(data: List[str], filename: str = "flight_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_from_file(filename: str = "flight_data.json") -> List[str]:
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    # Demo of generating inventory dataset
    inventory = generate_random_inventory(50)
    save_to_file(inventory)
    print("Generated and saved inventory data:", inventory)

    # Demo of generating flight dataset
    data = generate_flight_numbers()
    save_to_file(data)
    print("Generated flight numbers:", data)
