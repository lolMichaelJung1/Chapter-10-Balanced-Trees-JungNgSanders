# Chapter-10-Balanced-Trees-JungNgSanders
by Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# 🛠️ Objective:

- Explore AVL and Red-Black Trees.
- Implement basic AVL and Red-Black Trees in Python.
- Compare performance and balancing operations between the two structures.
- Reflect on design choices through coding, visualization, and analysis.

# 🧹 Lab

## Part 1: AVL Tree Implementation
- Implement a basic AVL Tree class in Python.
- Support insertion with rebalancing (rotations).
- Include tree printing (simple text output or graphic).
- Real-life scenario to model with your AVL Tree:  Organizing inventory stock numbers for a warehouse.


## Part 2: Red-Black Tree Implementation
- Implement a Red-Black Tree class in Python.
- Support insertion with recoloring and rotation as needed.
- Include tree printing (simple text output or graphic).
- Real-life scenario to model with your Red-Black Tree: Managing airline flight numbers for efficient look-up and updates.

## 📁 Project Structure (AVL & RBT)
'''
warehouse-inventory/
├── avl/
│   ├── node.py              # AVLNode class
│   └── tree.py              # AVLTree logic
├── rbtree/
│   ├── node.py              # RedBlackNode class
│   └── tree.py              # RedBlackTree logic
├── data/
│   ├── generate_data.py     # Random inventory data
│   └── generate_flight_data.py # Random flight data
├── inventory/
│   └── manager.py           # InventoryManager abstraction
├── flights/
│   └── manager.py           # FlightManager abstraction
├── tests/
│   ├── test_avl_tree.py     # Unit tests for AVL
│   └── test_rbtree.py       # Unit tests for RBT
├── main.py                  # Inventory app entry point
├── main_flights.py          # Flight app entry point
└── README.md                # Project documentation
'''
## Part 3: Comparison and Analysis
- Insert the same set of 20 random integers into both trees.
- Track and report:
      a. Number of rotations
      b. Final tree heights
      c. Summarize key differences observed between the AVL and Red-Black trees.
