# Chapter-10-Balanced-Trees-JungNgSanders
by Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# 🛠️ Objective:
- Explore AVL and Red-Black Trees.
- Implement basic AVL and Red-Black Trees in Python.
- Compare performance and balancing operations between the two structures.
- Reflect on design choices through coding, visualization, and analysis.

# 🧹 Lab
## Overall Demo
- A demo of all functionality may be found in the `main_demo.py` file, which incorporates all designed classes and executes the following scenarios
  - AVL Tree Random Insert Test
  - Inventory Manager Demo using AVL trees
  - Red-Black Tree Random Insert Test
  - Flight Manager Demo using Red-Black trees
- To run the demos, clone the repository and execute the following code from the repository root
```shell
python main_demo.py
```
- For convenience, a single consolidated file, `module10_lab.py`, has been created to allow for downloading and running all code demos within a single file
```shell
python module10_lab.py
```

## Part 1: AVL Tree Implementation
- Implement a basic AVL Tree class in Python.
- Support insertion with rebalancing (rotations).
- Include tree printing (simple text output or graphic).
- Real-life scenario to model with your AVL Tree:  Organizing inventory stock numbers for a warehouse.
#### Sample Usage
- To demonstrate the implementation of the AVL Tree class, insertion, rebalancing, and tree printing, run the following code
```shell
python AVLTree.py
```
- A truncated version of the sample output is shown below
```text
--- Running Example Usage ---


------- Demo of AVLTree: insert() with balancing (show balance factors) ------


------Balanced AVL Tree without Rotation------

Inserting 50 into AVL Tree:
... <output continues below>...
```

## Part 2: Red-Black Tree Implementation
- Implement a Red-Black Tree class in Python.
- Support insertion with recoloring and rotation as needed.
- Include tree printing (simple text output or graphic).
- Real-life scenario to model with your Red-Black Tree: Managing airline flight numbers for efficient look-up and updates.
#### Sample Usage
- To demonstrate the implementation of the Red-Black Tree class, insertion, recoloring, rotation, and tree printing, run the following code
```shell
python RedBlackTree.py
```
- A truncated version of the sample output is shown below
```text
Inserting values: [10, 20, 30, 15, 25, 5, 1, 8, 18, 28]

Inserting 10...
DEBUG: BstNode.__init__(10) called
Inorder Traversal (value, color): [(10, 'B')]

Inserting 20...
DEBUG: BstNode.__init__(20) called
Inorder Traversal (value, color): [(10, 'B'), (20, 'R')]
...<output continues below>...
```

## Part 3: Comparison and Analysis
- Insert the same set of 20 random integers into both trees.
- Track and report:
      a. Number of rotations
      b. Final tree heights
      c. Summarize key differences observed between the AVL and Red-Black trees.

## 📁 Project Structure (AVL & RBT)
```
warehouse-inventory/airline-flight
├── avl_node.py                    # AVLNode class
├── AVLTree.py                     # AVLTree logic
├── red_black_node.py              # RedBlackNode class
├── RedBlackTree.py                # RedBlackTree logic
├── generate_data.py               # Random flight data & inventory data
├── avl_inventory_manager.py       # InventoryManager abstraction
├── rbt_flight_manager.py          # FlightManager abstraction
├── tests/
│   ├── test_avl_tree.py           # Unit tests for AVL Tree and Node
│   └── test_rbtree.py             # Unit tests for RBT Tree and Node
├── main_demo.py                   # Entry point for Inventory Manager and Flight Manager demos
├── module10_lab.py                # Convenience file for all class definitions
└── README.md                      # Project documentation

