from typing import OrderedDict
from ps3 import BinarySearchTree
# from ps3_solution import BinarySearchTree


class Debugger:
    def __init__(self):
        self.counter = 0
        self._size_counter = 0
    
    def clear(self):
        self.counter = 0
        self._size_counter = 0

    def inc(self):
        self.counter += 1

    def count(self):
        return self.counter

    def inc_size_counter(self):
        self._size_counter += 1

    def size_counter(self):
        return self._size_counter


def multi_getattr(obj, attr, default=None):
    """
    Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is
    equivalent to x.a.b.c.d. When a default argument is given, it is
    returned when any attribute in the chain doesn't exist; without
    it, an exception is raised when a missing attribute is encountered.

    """
    attributes = attr.split(".")
    for i in attributes:
        try:
            obj = getattr(obj, i)
        except AttributeError:
            return default
    return obj


def init_tree(key):
    T = BinarySearchTree()
    T.debugger = Debugger()
    T.key = key
    return T


def construct_tree_example():
    T = BinarySearchTree()
    T.debugger = Debugger()
    T.key = 4
    T.insert(2)
    T.insert(6)
    T.insert(3)
    T.insert(1)
    T.insert(80)
    T.insert(60)
    # T.print_bst()
    return T


def IsSearchTreePropertyMaintained(T):
    leftCon = True
    rightCon = True
    if T.left is not None:
        if T.left.key > T.key:
            return False
        leftCon = IsSearchTreePropertyMaintained(T.left)
    if T.right is not None:
        if T.right.key < T.key:
            return False
        rightCon = IsSearchTreePropertyMaintained(T.right)
    return leftCon and rightCon

def get_height_of_tree(T):
    left_height = 0
    right_height = 0
    if T.right is not None:
        left_height = get_height_of_tree(T.right)
    if T.left is not None:
        right_height = get_height_of_tree(T.left)
    return max(left_height, right_height) + 1

def test():
    # Search
    # Insert
    # Select
    # Deletion
    # Rotation

    tests = OrderedDict()

    tests["Problem 1 Tests (requires insert to work):"] = [
        {
            "label": "Basic Search 1.1a",
            "input": construct_tree_example(),
            "test": lambda T: getattr(construct_tree_example().search(1), "key", None),
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1a",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(1), "key", None),
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1b",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(2), "key", None),
            "expected": 2,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1c",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(3), "key", None),
            "expected": 3,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1d",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(4), "key", None),
            "expected": 4,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1e",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(6), "key", None),
            "expected": 6,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1f",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(60), "key", None),
            "expected": 60,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1f",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.search(80), "key", None),
            "expected": 80,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1g",
            "input": construct_tree_example(),
            "test": lambda T: T.search(21),
            "expected": None,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1h",
            "input": construct_tree_example(),
            "test": lambda T: T.search(-2),
            "expected": None,
            "show_expectation": True
        },
        {
            "label": "Basic Search 1.1i",
            "input": construct_tree_example(),
            "test": lambda T: T.search(1000),
            "expected": None,
            "show_expectation": True
        },
        #
        #
        #
        # {
        #     "label": "Basic Insert 1.2a (Size: 1 | Height: " + str(get_height_of_tree(init_tree(4))) + ")",
        #     "input": init_tree(4),
        #     "test": lambda T: T.size,
        #     "expected": 1,
        #     "show_expectation": True,
        #     "count_calculate_sizes": True,
        # },
        {
            "label": "Basic Insert 1.2b (Size: 2 | Height: " + str(get_height_of_tree(init_tree(4))) + ")",
            "input": init_tree(4),
            "test": lambda T: T.insert(1).size,
            "expected": 2,
            "show_expectation": True,
            "count_calculate_sizes": True,
        },
        {
            "label": "Basic Insert 1.2c (Size: 3 | Height: " + str(get_height_of_tree(init_tree(4).insert(1))) + ")",
            "input": init_tree(4).insert(1),
            "test": lambda T: T.insert(8).size,
            "expected": 3,
            "show_expectation": True,
            "count_calculate_sizes": True,
        },
        {
            "label": "Basic Insert 1.2c (Size: 3 | Height: " + str(get_height_of_tree(init_tree(4).insert(1))) + ")",
            "input": init_tree(4).insert(1),
            "test": lambda T: T.insert(2).size,
            "expected": 3,
            "show_expectation": True,
            "count_calculate_sizes": True,
        },
        {
            "label": "Basic Insert 1.2d (Size: 9 | Height: " + str(get_height_of_tree(init_tree(4).insert(1).insert(2).insert(3).insert(5).insert(6).insert(7).insert(8))) + ")",
            "input": init_tree(4).insert(1).insert(2).insert(3).insert(5).insert(6).insert(7).insert(8),
            "test": lambda T: T.insert(9).size,
            "expected": 9,
            "show_expectation": True,
            "count_calculate_sizes": True,
        },
        {
            "label": "Basic Insert 1.2d (Size: 15 | Height: " + str(get_height_of_tree(init_tree(4).insert(1).insert(2).insert(3).insert(5).insert(6).insert(7).insert(8).insert(9).insert(10).insert(11).insert(12).insert(14))) + ")",
            "input": init_tree(4).insert(1).insert(2).insert(3).insert(5).insert(6).insert(7).insert(8).insert(9).insert(10).insert(11).insert(12).insert(14),
            "test": lambda T: T.insert(15).size,
            "expected": 14,
            "show_expectation": True,
            "count_calculate_sizes": True,
        },
        #
        #
        #
        {
            "label": "Basic Select 1.3a",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.select(0), "key", None),
            "expected": 1,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3b",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.select(1), "key", None),
            "expected": 2,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3c",
            "input": construct_tree_example(), 
            "test": lambda T: getattr(T.select(2), "key", None),
            "expected": 3,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3d",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.select(3), "key", None),
            "expected": 4,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3e",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.select(4), "key", None),
            "expected": 6,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3f",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.select(5), "key", None),
            "expected": 60,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3f",
            "input": construct_tree_example(),
            "test": lambda T: getattr(T.select(6), "key", None),
            "expected": 80,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3g",
            "input": construct_tree_example(),
            "test": lambda T: T.select(7),
            "expected": None,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3h",
            "input": construct_tree_example(),
            "test": lambda T: T.select(8),
            "expected": None,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3i",
            "input": construct_tree_example(),
            "test": lambda T: T.select(-1),
            "expected": None,
            "show_expectation": True
        },
        {
            "label": "Basic Select 1.3j",
            "input": construct_tree_example(),
            "test": lambda T: T.select(-20),
            "expected": None,
            "show_expectation": True
        },
    ]
    
    for label, test_results in tests.items():
        print(label)

        for i, result in enumerate(test_results):
            # Print passed with test number and name
            # If failed, print failed and pring the expected and recieved values
            result["input"].debugger.clear()
            res = result["test"](result["input"])
            con = res == result["expected"]
            print(result["label"] + ": ", "Passed" if con else "Failed", end="")
            if (not con and ("show_expectation" not in result or result["show_expectation"])):
                print(" - Expected " +
                      str(result["expected"]) + " But Got " + str(res), end="")
            print()
            print("\t Is Search Tree Property is Maintained? " +
                  str(IsSearchTreePropertyMaintained(result["input"])))
            if ("count_calculate_sizes" in result and result["count_calculate_sizes"]):
                # print("\t Number of calls to calculate_sizes: " +
                #       str(result["input"].debugger.count()))
                print("\t Number of sets/changes to to tree node sizes: " +
                      str(result["input"].debugger.size_counter()))
            print()

        print()


if __name__ == "__main__":
    test()
