# C++ Programming Laboratory & Concept Exercises

Welcome to the **C++** section of the College Project repository. This directory contains a curated set of C++ programs designed to demonstrate fundamental programming constructs and Core Object-Oriented Programming (OOP) concepts such as encapsulation, constructors, access control, and friend functions.

---

## 📂 File Catalog & Concepts Demonstrated

Each file is designed as a standalone demonstration of specific C++ language features. Here is an overview of what each program does and the concepts it illustrates:

| File Name | Description | Key OOP & Programming Concepts |
| :--- | :--- | :--- |
| **`eg.cpp`** | A minimal "Hello World" program that prints a message to the console. | Basic Syntax, I/O streams (`std::cout`). |
| **`StudentClass.cpp`** | Defines a `Student` class that manages basic student info (Name, Age, and Percentage). | Data Encapsulation, Private Helper Methods (`getData()`), Public Interface (`displayData()`). |
| **`EmployeeClass.cpp`** | Models an `Employee` with gross salary calculation logic (`basic_sal + 0.6 * basic + 0.4 * basic`). | Member Methods, Private Member Input (`getInfo()`), Access Specifiers, and Mathematical Operations. |
| **`ComplexClasswithConstructor.cpp`** | Represents Complex Numbers and implements addition using object parameters and returns. | Default & Parameterized Constructors, Object as Function Parameters, Returning Objects. |
| **`FriendFunction.cpp`** | Represents Complex Numbers and implements addition using an external non-member friend function. | Non-member access, the `friend` keyword, Data Sharing across objects. |
| **`Demo.cpp`** | A class-based utility program that takes a number and runs multiple mathematical and logical tests. | Loops (`for`/`while`), algorithms (Factorial, Reversal, Palindrome verification, and Armstrong verification). |
| **`tempCodeRunnerFile.cpp`** | A temporary file containing a simple program to compute the sum of two user-input integers. | Basic standard input/output (`std::cin`, `std::cout`) and arithmetic. |

---

## 🔍 Detailed Program Breakdown

### 1. Basic Structure & Syntax
* **`eg.cpp`**: 
  A standard sanity-check program. It uses `#include<iostream>` and `using namespace std;` to write `"Hello World"` to the standard console output.

### 2. Encapsulation & Private Helper Methods
* **`StudentClass.cpp`** & **`EmployeeClass.cpp`**:
  * These classes hide their member variables (`name`, `age`, `percentage`, `basic_sal`) in the private section.
  * They demonstrate **private helper methods** (`Student::getData()` and `Employee::getInfo()`) that are only callable inside the class.
  * This is an excellent showcase of the *Principle of Least Privilege* in object-oriented design—the external user (in `main()`) only has permission to call the public methods (`displayData()` / `displayInfo()`), which internally handle resource acquisition and validation.

### 3. Object Initialization via Constructors
* **`ComplexClasswithConstructor.cpp`**:
  * Demonstrates the **Default Constructor** (`Complex()`) which initializes real and imaginary values to 0.
  * Demonstrates the **Parameterized Constructor** (`Complex(float r, float i)`) for custom initialization.
  * Demonstrates passing another `Complex` object to the `sum()` method to calculate and return a new `Complex` object.

### 4. Bypassing Strict Encapsulation with Friend Functions
* **`FriendFunction.cpp`**:
  * Standard access rules prevent external (non-member) functions from accessing a class's private members.
  * Here, the non-member function `Complex sum(Complex, Complex)` is granted access using the `friend` specifier inside the class body. This allows it to directly read/write `real` and `imag` properties of passing objects, illustrating how to extend class interaction without standard inheritance or member declaration.

### 5. Mathematical Algorithms in Classes
* **`Demo.cpp`**:
  * An algorithm-dense file featuring loop control and digits manipulation:
    * **Factorial**: Finds $n!$ using a simple multiplication loop.
    * **Number Reversal**: Reverses the digits of $n$ using modulo and division arithmetic.
    * **Palindrome**: Validates if the number is identical when reversed.
    * **Armstrong Number**: Computes the sum of each digit raised to the power of the count of digits and checks if it equals the original number.

---

## 🚀 How to Compile & Run

You can compile these files using any standard C++ compiler, such as `g++` (GCC) or `clang++`. 

### Command Line Instructions:

1. **Open your terminal** and navigate to this folder:
   ```bash
   cd College_Project_Files/C++
   ```

2. **Compile a file** (e.g., `Demo.cpp`):
   ```bash
   g++ Demo.cpp -o Demo.exe
   ```

3. **Execute the compiled binary**:
   * **Windows**:
     ```cmd
     Demo.exe
     ```
   * **Linux / macOS**:
     ```bash
     ./Demo
     ```

---

## 📝 Miscellaneous Notes

* **Build Outputs (`.exe`)**: The `.exe` files present in this directory are compiled executable binaries for Windows. They can be safely deleted or excluded from source control (using `.gitignore`) as they can be reconstructed from source `.cpp` files at any time.
* **Temporary Files (`tempCodeRunnerFile.cpp`)**: This file is auto-generated by the popular VS Code *Code Runner* extension when you highlight/run partial blocks of code. It contains a simple sum program and can be safely ignored or cleaned up.
