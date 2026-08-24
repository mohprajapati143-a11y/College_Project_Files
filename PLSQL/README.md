# 🗄️ PL/SQL Database Programming Lab

Welcome to the **PL/SQL** (Procedural Language for SQL) laboratory. This directory contains a comprehensive collection of Oracle PL/SQL scripts, ranging from basic anonymous blocks and variable operations to advanced database concepts like cursors, collections (Varrays), and conditional triggers.

These scripts demonstrate how to extend standard SQL with procedural logic to build robust database-centric applications.

---

## 📂 File Catalog & Concepts Demonstrated

| File Name | Category | Primary PL/SQL Concept | Description |
| :--- | :--- | :--- | :--- |
| **`Print.sql`** | Core | Basic Output | Demonstrates the use of `DBMS_OUTPUT.PUT_LINE` to print text to the console. |
| **`operationvariable.sql`**| Core | Variable Operations | Shows declaration of variables, assignments, and basic arithmetic within a PL/SQL block. |
| **`Positive_Negative.sql`**| Logic | Branching | Evaluates if a number is positive, negative, or zero using `IF-THEN-ELSIF` logic. |
| **`Even_odd.sql`** | Logic | Conditional Logic | Checks the parity of an input number using the `MOD` function. |
| **`Greatest.sql`** | Logic | Comparisons | Finds the larger of two numbers using simple relational operators. |
| **`Greater_three.sql`** | Logic | Compound Logic | Identifies the maximum value among three variables using nested or compound conditions. |
| **`Multiple3_5.sql`** | Algorithms | Multiples | Checks if a number is a multiple of both 3 and 5. |
| **`Multiple3_7.sql`** | Algorithms | Multiples | Checks if a number is a multiple of both 3 and 7. |
| **`Factorial.sql`** | Algorithms | Iteration / Loops | Computes the factorial of a number using a standard `FOR` or `WHILE` loop. |
| **`Vowels.sql`** | Manipulation | String Parsing | Scans a string or character input to identify and count vowels. |
| **`Bcalculator.sql`** | Application | Basic Calculator | Implements a simple four-function calculator logic within a procedural block. |
| **`Varray.sql`** | Collections | Variable-Size Arrays | Demonstrates the use of `VARRAY` to store and iterate over a fixed-size collection of elements. |
| **`Cursor.sql`** | DB Ops | Explicit Cursors | Illustrates how to use cursors to process multiple rows returned by a query, including `OPEN`, `FETCH`, and `CLOSE` cycles. |
| **`Delete.sql`** | DB Ops | DML Operations | Shows how to safely execute `DELETE` statements within a PL/SQL block and handle row counts. |
| **`Result.sql`** | Logic | Grade Calculation | Takes marks as input and determines the student's result/grade based on predefined ranges. |
| **`Q_14.sql`, `Q_15.sql`, `Q_16.sql`** | Exercises | Structured Problems | Specific lab exercise implementations covering various mixed concepts from cursors to record updates. |

---

## 🔍 Detailed Concept Breakdown

### 1. The PL/SQL Block Structure
Every script follows the standard Oracle PL/SQL block architecture:
- **`DECLARE`**: (Optional) Where variables, constants, cursors, and user-defined types are defined.
- **`BEGIN`**: (Mandatory) The execution section containing the procedural and SQL statements.
- **`EXCEPTION`**: (Optional) Where runtime errors are caught and handled.
- **`END;`**: (Mandatory) Signifies the end of the block.

### 2. Working with Database Collections
* **`Varray.sql`**:
  * Shows how to define a `TYPE ... IS VARRAY(n) OF ...`.
  * Demonstrates how to initialize the array and access elements using 1-based indexing, which is characteristic of PL/SQL.

### 3. Cursor Management
* **`Cursor.sql`**:
  * Explains the difference between implicit and explicit cursors.
  * Shows how to handle query results that return more than one row, which cannot be handled by a simple `SELECT INTO` statement.

---

## 🚀 How to Run and Test

### Prerequisites
You need access to an Oracle Database environment (such as **Oracle SQL*Plus**, **Oracle SQL Developer**, or **Oracle Live SQL**).

### Executing a Script
If using **SQL*Plus**, you can run a script using the `@` command:

1. Open your terminal or SQL*Plus console.
2. Connect to your database instance.
3. Enable output printing:
   ```sql
   SET SERVEROUTPUT ON;
   ```
4. Execute the script:
   ```sql
   @Factorial.sql
   ```

*Note: Ensure you have `SET SERVEROUTPUT ON;` enabled at the start of your session, otherwise `DBMS_OUTPUT` messages will not be visible in the console.*
