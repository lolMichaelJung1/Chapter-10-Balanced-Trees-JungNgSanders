import random
import json
from typing import List

def generate_random_inventory(count: int = 100, seed: int = 42) -> List[int]:
    random.seed(seed)
    return random.sample(range(1000, 9999), count)

def save_to_file(data: List[int], filename: str = "inventory_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_from_file(filename: str = "inventory_data.json") -> List[int]:
    with open(filename, 'r') as f:
        return json.load(f)


# Demo Usage
if __name__ == "__main__":
    inventory = generate_random_inventory(50)
    save_to_file(inventory)
    print("Generated and saved inventory data:", inventory)

