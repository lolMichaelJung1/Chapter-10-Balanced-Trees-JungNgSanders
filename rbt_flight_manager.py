# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/1/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
from red_black_node import RedBlackTreeNode
from RedBlackTree import RedBlackTree

class FlightManager:
    """
    Manages flight schedules using a Red-Black Tree.
    """
    def __init__(self):
        self.tree = RedBlackTree()

    def schedule_flight(self, flight_id):
        """Schedule a flight."""
        print(f"Scheduling flight {flight_id}")
        self.tree.insert(flight_id)

    def display_flight_schedule(self, node=None, level=0, prefix='Root:'):
        """Display the flight schedule tree."""
        print("\n--- Flight Schedule Tree ---")
        self.tree.print_tree(node or self.tree.root, level, prefix)

    def print_operations_log(self):
        """Print the operation log."""
        self.tree.print_log()


# === Demo ===
if __name__ == "__main__":
    manager = FlightManager()
    flight_ids = random.sample(range(1000, 2000), 10)
    for fid in flight_ids:
        manager.schedule_flight(fid)

    manager.display_flight_schedule()
    manager.print_operations_log()
