class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert(current_node.right, value)

    def update(self, node, oldValue, newValue):
        if node:
            self.update(node.left, oldValue, newValue)
            if (node.value == oldValue):
                node.value = newValue
                return
            self.update(node.right, oldValue, newValue)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.inorder(node.right)

    def printTree(self, node):
        if node:
            self.printTree(node.left)
            print(node.value, end=" ")
            self.printTree(node.right)


tree = BinaryTree(5)  # Root node is 5
for i in range(3, 10):
    tree.insert(tree.root, i)

print("==========================")
print("Inorder ")
tree.printTree(tree.root)
print("\n==========================")
tree.update(tree.root, 6, 10)
print("After update...")
tree.printTree(tree.root)
print("\n==========================")