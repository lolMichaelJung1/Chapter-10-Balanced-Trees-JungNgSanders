import pytest
from AVLTree import AVLTree
from avl_node import AvlNode

@pytest.fixture
def avl_tree():
    return AVLTree()

def insert_values(tree, values):
    for value in values:
        tree.insert(value)

def test_single_insertion(avl_tree):
    avl_tree.insert(10)
    assert avl_tree.root is not None
    assert avl_tree.root.value == 10

def test_balanced_insertion(avl_tree):
    insert_values(avl_tree, [30, 20, 40])
    assert avl_tree.root.value == 30
    assert avl_tree.root.left.value == 20
    assert avl_tree.root.right.value == 40

def test_left_rotation(avl_tree):
    insert_values(avl_tree, [10, 20, 30])  # Causes left rotation
    assert avl_tree.root.value == 20

def test_right_rotation(avl_tree):
    insert_values(avl_tree, [30, 20, 10])  # Causes right rotation
    assert avl_tree.root.value == 20

def test_left_right_rotation(avl_tree):
    insert_values(avl_tree, [30, 10, 20])  # Causes left-right rotation
    assert avl_tree.root.value == 20

def test_right_left_rotation(avl_tree):
    insert_values(avl_tree, [10, 30, 20])  # Causes right-left rotation
    assert avl_tree.root.value == 20

def test_duplicate_insertion(avl_tree):
    insert_values(avl_tree, [50, 30, 70])
    avl_tree.insert(50)  # Duplicate
    assert any("duplicated key 50" in msg.lower() for msg in avl_tree.log)
    assert avl_tree.root.value == 50

def test_rotation_count(avl_tree):
    insert_values(avl_tree, [10, 20, 30])
    assert avl_tree.rotation_count > 0

def test_log_population(avl_tree):
    insert_values(avl_tree, [10, 20, 30])
    assert any("rotation" in entry.lower() for entry in avl_tree.log)

def test_avl_node_inherits_bst_node():
    node = AvlNode(5)
    assert hasattr(node, "value")
    assert hasattr(node, "left")
    assert hasattr(node, "right")
    assert hasattr(node, "parent")

def test_avl_node_initial_height():
    node = AvlNode(10)
    assert node.height == 1

def test_avl_node_debug_flag_false_by_default():
    node = AvlNode(15)
    assert not node.debug

def test_avl_node_debug_true_prints_debug_message(capsys):
    node = AvlNode(20, debug=True)
    captured = capsys.readouterr()
    assert "DEBUG: AvlNode.__init__(20) calling super()" in captured.out

def test_avl_node_str_method():
    node = AvlNode(42)
    assert str(node) == "42 (height: 1)"
