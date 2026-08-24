# 📂 Python Data Structures & Algorithms Lab

Welcome to the **Data Structures & Algorithms (DSA)** implementation laboratory in Python. This directory contains structured implementations of fundamental computer science data structures (including linear lists, stacks, queues, hash tables, trees, and graphs) and their corresponding manipulation algorithms.

These implementations are developed with clean Python syntax to serve as reference materials for academic study and foundational understanding of memory layouts, traversal strategies, and algorithm complexity.

---

## 📂 File Catalog & Concepts Demonstrated

| File Name | Category | Primary Data Structure / Concept | Description |
| :--- | :--- | :--- | :--- |
| **`Node_Class.py`** | Foundation | Linked Nodes | Defines a standardized `Node` class containing a value and pointer placeholder. Serves as the basic building block for linked lists, stacks, queues, and tree structures. |
| **`Stack.py`** | Linear ADT | LIFO Stack | Implements a classic Last-In-First-Out (LIFO) stack with complete support for `push()`, `pop()`, `peek()`, checking empty status, and displaying elements. |
| **`Queue.py`** | Linear ADT | FIFO Queue | Implements a First-In-First-Out (FIFO) queue utilizing list representation, including standard `enqueue()`, `dequeue()`, `peek()`, and queue traversal. |
| **`DoublyLinked_list.py`** | Linear ADT | Doubly Linked List | Implements a bidirectional linked list where each node has a reference to both its next and previous neighbors. Demonstrates insertion, deletion, and forward/backward traversal. |
| **`Polynomial.py`** | Application | Polynomial Addition ADT | Models algebraic polynomial terms ($c \cdot x^e$) using linked nodes, supporting automated sorting of exponents and adding polynomials of varying degrees. |
| **`Expression.py`** | Application | Expression Parsing | Handles mathematical/logical expression validation or parsing using stack structures to match parentheses and track operators. |
| **`Infix,Prefix,Postfix.py`** | Application | Expression Conversion | Implements the classical Shunting-Yard algorithm or equivalent logic to convert standard **Infix** mathematical expressions to **Postfix** and **Prefix** notations using a stack. |
| **`Hash.py`** | Associative | Hash Table & Mapping | Implements a key-value Hash Map from scratch. Demonstrates hashing functions, bucket indexing, and collision resolution mechanisms (such as chaining or linear probing). |
| **`Binary Seach Tree.py`** | Non-Linear | Binary Search Tree (BST) | Implements standard binary search tree structures. Includes ordered insertion, search lookups, and three classical tree traversals (**Inorder**, **Preorder**, and **Postorder**). |
| **`AVL Tree.py`** | Non-Linear | Self-Balancing BST | Implements an AVL Tree which maintains strict $O(\log n)$ heights through balancing. Features automatic rotations (**LL**, **RR**, **LR**, **RL**) upon insertion. |
| **`Graph.py`** | Non-Linear | Graphs | Implements graph topologies (using Adjacency Lists or Matrices). Covers basic structural creation and fundamental traversals: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. |
| **`STUDENT_RECORD.py`** | Application | CRUD Record System | Implements a records-database ADT for students (handling name, roll number, marks) supporting additions, modifications, deletions, and custom reports. |
| **`EMPLOYEE_RECORD.py`** | Application | CRUD Record System | Implements an interactive Employee directory utilizing dynamic dictionary bindings to create, update, delete, and view employee records. |

---

## 🔍 Detailed Program Breakdown

### 1. Linear Data Structures (Stacks & Queues)
* **`Stack.py` & `Queue.py`**:
  * **Stack**: Operates on a single-pointer basis (Top). It provides $O(1)$ updates at the top of the stack.
  * **Queue**: Operates with two boundary indices (Front and Rear). Demonstrates the sequential nature of job queues, buffers, and scheduling mechanisms.

### 2. Bidirectional Linked Structures
* **`DoublyLinked_list.py`**:
  * In contrast to Singly Linked Lists, this class contains reference pointers to both `next` and `prev`.
  * Demonstrates how nodes can be inserted or deleted at arbitrary positions without traversing from the head element, as well as enabling reverse scans of lists.

### 3. Tree Implementations & Automatic Balancing
* **`Binary Seach Tree.py`**:
  * Demonstrates hierarchical searching where left children are less than parent keys and right children are greater.
  * Illustrates **Recursion** for both insertion and traversals (Inorder traversal prints elements in sorted order).
* **`AVL Tree.py`**:
  * Extends the BST pattern. Standard BSTs can degenerate into $O(n)$ linked lists under sorted input.
  * The AVL tree tracks node heights and computes the **Balance Factor** (Height of Left Subtree - Height of Right Subtree).
  * If the factor exceeds the range $[-1, 1]$, LL/RR single rotations or LR/RL double rotations are executed dynamically to re-balance the tree, guaranteeing $O(\log n)$ search limits.

### 4. Graph Traversals
* **`Graph.py`**:
  * Models networks of vertices connected by edges.
  * **DFS**: Uses backtracking (relying on an implicit/explicit stack) to explore branches as deeply as possible first.
  * **BFS**: Uses a queue to scan vertices layer-by-layer, which is essential for finding the shortest path in unweighted graphs.

---

## 🚀 How to Run and Test

### Prerequisites
Make sure you have **Python 3.x** installed on your operating system. No third-party packages are required since these are pure Python standard library implementations.

### Running a Script
Open your terminal or command prompt, navigate to this directory, and execute the desired script:

```bash
# Example: Run the AVL Tree demo
python "AVL Tree.py"

# Example: Run the Doubly Linked List demo
python "DoublyLinked_list.py"

# Example: Run the Employee Record manager
python "EMPLOYEE_RECORD.py"
```

*Note: For files with spaces or commas in their names, make sure to wrap the filename in quotation marks as shown above.*
