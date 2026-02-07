#include <iostream>
#include <iomanip>
using namespace std;

void displayMenu() {
    cout << "\n========== SIMPLE CALCULATOR ==========" << endl;
    cout << "Operations:" << endl;
    cout << "  + : Addition" << endl;
    cout << "  - : Subtraction" << endl;
    cout << "  * : Multiplication" << endl;
    cout << "  / : Division" << endl;
    cout << "  % : Modulus" << endl;
    cout << "  q : Quit" << endl;
    cout << "========================================\n" << endl;
}

double calculate(double num1, char op, double num2) {
    switch(op) {
        case '+': return num1 + num2;
        case '-': return num1 - num2;
        case '*': return num1 * num2;
        case '/':
            if (num2 == 0) {
                cout << "Error: Division by zero!" << endl;
                return 0;
            }
            return num1 / num2;
        case '%':
            if (num2 == 0) {
                cout << "Error: Modulus by zero!" << endl;
                return 0;
            }
            return (int)num1 % (int)num2;
        default:
            cout << "Invalid operator!" << endl;
            return 0;
    }
}

int main() {
    char op;
    double num1, num2, result;
    char continueCalc;

    displayMenu();

    while (true) {
        cout << "Enter operator (+, -, *, /, %, q to quit): ";
        cin >> op;

        if (op == 'q' || op == 'Q') {
            cout << "Thank you for using the calculator. Goodbye!" << endl;
            break;
        }

        cout << "Enter first number: ";
        cin >> num1;
        
        cout << "Enter second number: ";
        cin >> num2;

        result = calculate(num1, op, num2);
        
        if (op == '/' || op == '%') {
            if (num2 != 0) {
                cout << fixed << setprecision(2);
                cout << "\n" << num1 << " " << op << " " << num2 << " = " << result << "\n" << endl;
            }
        } else if (op == '+' || op == '-' || op == '*') {
            cout << fixed << setprecision(2);
            cout << "\n" << num1 << " " << op << " " << num2 << " = " << result << "\n" << endl;
        }
    }

    return 0;
}