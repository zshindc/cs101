# adapted from binary_tree.py and test_binary_tree.py
# https://github.com/laurentluce/python-algorithms

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right


if __name__ == "__main__":
    tree = Node(10)
    for i in [5, 7, 15, 4, 13, 17]:
        tree.insert(i)
    for d in tree.tree_data():
        print(d)