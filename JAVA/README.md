# ☕ Object-Oriented Programming (OOP) in Java

Welcome to the **Java Programming** directory. This folder is dedicated to demonstrating key programming practices, data formatting, algorithmic thinking, and fundamental concepts of Object-Oriented Programming (OOP) in Java.

The exercises contained within range from core scalar logic to inheritance structures, showing how Java's compiled, type-safe architecture structures application classes.

---

## 📂 File Catalog & Concepts Demonstrated

| File Name | Primary Concept | Description | Key OOP & Programming Elements |
| :--- | :--- | :--- | :--- |
| **`AddBinary.java`** | Algorithm | Adds two binary representations of numbers together. | Input parsing, string arithmetic, binary systems. |
| **`AutoboxingEx.java`** | Type System | Shows wrapper classes converting primitive types automatically. | Autoboxing, Auto-unboxing, Wrapper classes (`Integer`). |
| **`CircleMetrics.java`** | Logic / I/O | Computes the area and perimeter of a circle dynamically. | `java.util.Scanner`, static library constants (`Math.PI`). |
| **`CircleMain.java`** | OOP Objects | Models a reusable custom Circle class with getter calculations. | Class instantiation, object states, encapsulation. |
| **`CountElements.java`** | Algorithms | Scans input strings, sorting characters into letters, digits, or spaces. | Iteration over char arrays, character predicates. |
| **`DecimalToBinary.java`** | Arithmetic | Standard algorithmic parser converting decimal bases to binary bases. | Loop iterations, string builders, division mechanics. |
| **`Demo.java`** | Utility | General purpose entry class illustrating simple console actions. | Primary execution paths, program checks. |
| **`DisplayPattern.java`** | Loops | Prints structured spatial text patterns onto the console. | Double-nested loops (`for`), coordinate print alignments. |
| **`MatrixMultiply.java`** | Arrays | Multiplies two multidimensional matrices. | Nested matrices, index constraints, standard matrix algebra. |
| **`MinMaxArray.java`** | Algorithms | Scans single-dimensional user arrays to find minimum/maximum boundaries. | Dynamic array allocation, item lookups, extreme values. |
| **`MultiplicationTable.java`** | Iteration | Formats and prints mathematical multiplication tables up to a limit. | Formatted loops, iterative multipliers. |
| **`ReverseString.java`** | Manipulation | Reverses letters of an input string in-place. | `StringBuilder`, backward looping, indexing. |
| **`StringMethods.java`** | String API | Demonstrates comprehensive Java string manipulation APIs. | `.length()`, `.concat()`, `.replace()`, `.substring()`, comparisons. |
| **`StudentRegistration.java`**| OOP Design | Models a registration system tracking academic names and details. | Constructor parameters, private field getters/setters. |
| **`StudentMain.java`** | OOP Objects | Class instantiator executing registration entities. | Object arrays, multi-student instances. |
| **`SumOfDigits.java`** | Arithmetic | Iteratively extracts digits of an integer to find their total sum. | Mathematical division, modulo operations (`%`). |
| **`SingleInheritanceDemo.java`**| OOP Inheritance | Implements simple, direct parent-to-child inheritance. | The `extends` keyword, basic class hierarchy. |
| **`MultilevelDemo.java`** | OOP Inheritance | Implements multi-tier class trees (e.g., Grandparent $\rightarrow$ Parent $\rightarrow$ Child). | Grandparent constructors, method inheritance, hierarchies. |
| **`HierarchicalDemo.java`** | OOP Inheritance | Implements single-parent, multi-child structural architectures. | Multiple sibling classes deriving from one base class. |

---

## 🔍 Detailed Concept Breakdown

### 1. Object-Oriented Principles & Inheritance
Java is strictly class-based. The inheritance demos show how code can be reused and structured hierarchically:
* **`SingleInheritanceDemo.java`**: Focuses on a single-child class extending a single-parent class, showcasing how the child acquires public and protected fields automatically.
* **`MultilevelDemo.java`**: Explores linear depth, where a class inherits from an intermediate class, which in turn inherits from a root parent class, showing how traits flow down the entire line.
* **`HierarchicalDemo.java`**: Sets up branches where different child classes inherit from the same base class, demonstrating how specialized child types share a common foundation.

### 2. Primitive Boxing & Wrapper Classes
* **`AutoboxingEx.java`**:
  * Explains how Java automatically transitions between raw primitives (like `int`) and their corresponding OOP wrapper classes (like `Integer`).
  * Autoboxing converts primitives into wrapper objects automatically (`Integer n2 = a;`), while Autounboxing retrieves the raw primitive values effortlessly (`int b = n3;`).

### 3. Comprehensive String Manipulations
* **`StringMethods.java` & `CountElements.java`**:
  * Strings are objects in Java, not array structures of bytes.
  * Shows how to inspect, slice, compare, and parse text securely using standard Java APIs.
  * Demonstrates the use of character wrappers (`Character.isLetter()`, `Character.isDigit()`) to evaluate single-character properties.

---

## 🚀 How to Compile and Run

### Prerequisites
Make sure you have the **Java Development Kit (JDK)** installed (JDK 8 or higher is recommended) and the paths are added to your environment variables (`javac` and `java` commands should be available).

### Compiling a Program
Open your terminal in the `JAVA` folder and compile the source file using the Java compiler:

```bash
# Example: Compile SingleInheritanceDemo
javac SingleInheritanceDemo.java
```

This generates `.class` bytecode files (e.g., `SingleInheritanceDemo.class`).

### Executing a Program
Run the compiled class bytecode using the Java interpreter:

```bash
# Run the compiled bytecode
java SingleInheritanceDemo
```

*Note: Do not append `.class` to the filename when running the program using the `java` command.*
