# 🐍 Python Programming & Algorithmic Design Lab

Welcome to the **Python** laboratory section. This directory contains a diverse collection of Python scripts focusing on fundamental programming constructs, numerical algorithms, string matching techniques, and complex problem-solving strategies using recursion.

The exercises here are designed to transition from basic 1D/2D array manipulations to advanced algorithmic concepts like graph theory and spatial recursion.

---

## 📂 File Catalog & Concepts Demonstrated

| File Name | Category | Primary Concept | Description |
| :--- | :--- | :--- | :--- |
| **`eg.py`** | OOP | Classes & Composition | Demonstrates basic Class definitions, `__init__` constructors, and object composition (Employee has an Address). |
| **`1DArray.py`** | Data Handling | NumPy 1D Arrays | Uses the `numpy` library to create, index, modify, and iterate over one-dimensional arrays. |
| **`2DArray.py`** | Data Handling | NumPy 2D Arrays | Extends array concepts to matrices (2D), showing row-column indexing and nested iterations. |
| **`Factorial.py`** | Arithmetic | Iteration | A standard implementation to find the factorial ($n!$) using loop-based accumulation. |
| **`fibonacci.py`** | Algorithms | Sequences | Generates the Fibonacci sequence, demonstrating iterative progression and list handling. |
| **`Linear_search.py`** | Algorithms | Searching | Implements the $O(n)$ linear search algorithm to find an element within a list. |
| **`bubble.py`** | Algorithms | Sorting | Implements the **Bubble Sort** algorithm, showcasing nested loops and element swapping logic. |
| **`selection_sort.py`** | Algorithms | Sorting | Implements **Selection Sort**, demonstrating the search for minimum elements and positional swaps. |
| **`insertionSort.py`** | Algorithms | Sorting | Implements **Insertion Sort**, illustrating how elements are shifted to maintain a sorted sub-portion. |
| **`Navie_string_match.py`**| Algorithms | Pattern Matching | A raw implementation of the **Naive String Matching** algorithm to find pattern occurrences within a text string. |
| **`Stack.py`** | Data Structures | Linear ADT | A class-based or list-based implementation of a Stack (LIFO), featuring `push` and `pop` operations. |
| **`Tower_of_hanoi.py`** | Algorithms | Recursion | A classic recursive solution to the **Tower of Hanoi** puzzle, illustrating recursive depth and move counting. |
| **`Kruskal_Algorithm.py`** | Algorithms | Graph Theory | Implements **Kruskal's Algorithm** for finding the Minimum Spanning Tree (MST) of a weighted graph. |

---

## 🔍 Detailed Concept Breakdown

### 1. Modern Array Manipulation with NumPy
Python's standard lists are flexible, but for mathematical and scientific computing, **NumPy** is the industry standard.
* **`1DArray.py` & `2DArray.py`**:
  * Demonstrates the creation of high-performance arrays.
  * Shows how to perform "Vectorized" operations and use advanced indexing (like `array[1, 2]`) which is more efficient than standard list-of-lists indexing.

### 2. Sorting & Searching Algorithms
This laboratory covers the "Big Three" introductory sorting algorithms:
* **Bubble Sort**: Best for understanding the concept of "swapping" and "passes."
* **Selection Sort**: Efficiently reduces the number of swaps by finding the extreme value first.
* **Insertion Sort**: Mimics how humans sort playing cards in their hands, providing better performance for nearly sorted data.

### 3. Advanced Recursive Logic
* **`Tower_of_hanoi.py`**:
  * Solves the puzzle by breaking it into smaller sub-problems: "Move $n-1$ disks to the auxiliary peg, move the $n$-th disk to the target peg, then move the $n-1$ disks from the auxiliary peg to the target peg."
  * This script is an excellent example of how complex problems can be reduced to elegant, few-line recursive functions.

### 4. Graph Algorithms & Greedy Strategy
* **`Kruskal_Algorithm.py`**:
  * Demonstrates a **Greedy Algorithm** approach.
  * Sorts all edges by weight and adds them to the MST only if they don't form a cycle (using the Union-Find data structure).
  * This is a fundamental concept in networking and optimization problems.

---

## 🚀 How to Run and Test

### Prerequisites
Make sure you have **Python 3.x** installed. Some files (like the array scripts) require the **NumPy** library.

### Installing Dependencies
If you don't have NumPy, you can install it via `pip`:
```bash
pip install numpy
```

### Running a Script
Execute any script using the Python interpreter:

```bash
# Example: Run the Tower of Hanoi simulation
python Tower_of_hanoi.py

# Example: Run the Kruskal's Algorithm MST solver
python Kruskal_Algorithm.py
```
---
*Note: All scripts are developed to be standalone and can be executed independently in any standard Python environment.*
