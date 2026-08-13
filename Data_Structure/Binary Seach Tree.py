
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

# In-order Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Pre-order Traversal
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Post-order Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Main Program
root = None

n = int(input("Enter Number of Nodes: "))

for i in range(n):
    value = int(input("Enter Value: "))
    root = insert(root, value)

print("\nIn-order Traversal:")
inorder(root)

print("\nPre-order Traversal:")
preorder(root)

print("\nPost-order Traversal:")
postorder(root)
