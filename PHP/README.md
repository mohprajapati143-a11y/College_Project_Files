# 🐘 PHP Core Scripting & Web Utilities

Welcome to the **PHP** (Hypertext Preprocessor) scripting laboratory. This directory contains structured exercises demonstrating core server-side scripting patterns, basic arithmetic manipulation, logic structures, and standard web integrations.

These scripts illustrate how PHP executes server-side commands, interpolates data, and interfaces with HTML components to build simple dynamic web views.

---

## 📂 File Catalog & Concepts Demonstrated

| File Name | Category | Description | Primary Language Constructs |
| :--- | :--- | :--- | :--- |
| **`Print.php`** | Core Output | Demonstrates standard methods of printing output and rendering HTML from the server. | `echo` vs. `print`, variable interpolation, inline HTML. |
| **`Add.php`** | Arithmetic | Computes the sum of defined numbers, exploring variable declarations and mathematical operators. | Floating/integer types, concatenation, assignment operator. |
| **`EvenOdd.php`** | Branching | Receives or defines an integer and evaluates if it is even or odd. | Modulo operator (`%`), `if-else` control blocks. |
| **`Factorial.php`** | Loops | Calculates the factorial ($n!$) of a number using iterative loops. | `for`/`while` loops, accumulator variables. |
| **`Reverse.php`** | Manipulation | Reverses strings and integers demonstrating standard processing techniques. | String indices, length calculations (`strlen()`), reversing helper methods. |
| **`Calculator.php`** | Web Integration | A fully interactive dynamic web calculator integrating HTML forms with server-side processing. | `$_POST`/`$_GET` superglobals, form input parsing, multiple action handlers. |

---

## 🔍 Detailed Concept Breakdown

### 1. Server-Side Execution & Output Streams
* **`Print.php`**:
  * Shows how PHP scripts compile and execute on the server, sending the final plain HTML output downstream to the client's browser.
  * Highlights the semantic differences between `echo` (which acts as a language construct that can take multiple arguments) and `print` (which behaves like a function and returns a success value).

### 2. Multi-Functional Form Integration (HTTP Requests)
* **`Calculator.php`**:
  * Combines web interface (HTML structure) with backend calculations (PHP logic) in a single unified script.
  * Shows how PHP intercepts **HTTP POST** requests via the `$_POST` superglobal array.
  * Validates user inputs, retrieves form inputs, evaluates selected operators (`+`, `-`, `*`, `/`), and prints calculations back into the visual webpage template, avoiding complex multi-page routing.

---

## 🚀 How to Run and Test

### Option A: Local Command Line (PHP CLI)
If you only want to see the text execution of non-web files, run them using your command line terminal.

#### Prerequisites
Ensure the PHP interpreter is installed on your computer and the `php` path is added to your environment variables.

#### Running a Script
Open your terminal in the `PHP` folder and execute:

```bash
# Example: Run the even-odd check
php EvenOdd.php

# Example: Run the printing demo
php Print.php
```

---

### Option B: Local Web Server (Recommended for Calculator)
Since PHP is a server-side web scripting language, interactive scripts like `Calculator.php` are best run inside a local web server environment.

1. Open your terminal inside this directory (`College_Project_Files/PHP/`).
2. Start PHP's built-in lightweight development server:
   ```bash
   php -S localhost:8000
   ```
3. Open your favorite web browser and navigate to:
   ```
   http://localhost:8000/Calculator.php
   ```
4. Enter numbers and press the operational buttons to test the interactive server calculations.
