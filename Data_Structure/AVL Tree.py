# AVL Tree Implementation
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Get height
def getHeight(root):
    if not root:
        return 0
    return root.height

# Get balance factor
def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)

# Right rotate
def rightRotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

# Left rotate
def leftRotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

# Insert into AVL
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    # Rotations
    if balance > 1 and key < root.left.key:
        return rightRotate(root)
    if balance < -1 and key > root.right.key:
        return leftRotate(root)
    if balance > 1 and key > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and key < root.right.key:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

# In-order traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Driver code
root = None
dataset = [10, 20, 30, 40, 50, 25]
for key in dataset:
    root = insert(root, key)

print("In-order Traversal of Balanced AVL Tree:")
inorder(root)

import heapq

# Min-Heap Priority Queue
tasks = []
heapq.heappush(tasks, (2, "Job Scheduling"))
heapq.heappush(tasks, (1, "Patient Triage (High Priority)"))
heapq.heappush(tasks, (3, "Email Notification"))

print("\nPriority Queue (Min-Heap):")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority} -> {task}")
