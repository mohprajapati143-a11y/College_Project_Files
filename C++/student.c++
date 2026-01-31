#include <iostream>
using namespace std;

class BankEmployee {
private:
    string name;
    long account_no;
    float balance;

public:
    // Function to input employee details
    void getData() {
        cout << "Enter employee name: ";
        getline(cin, name);

        cout << "Enter account number: ";
        cin >> account_no;

        cout << "Enter initial balance: ";
        cin >> balance;
    }

    // Function to display details
    void display() {
        cout << "\n--- Employee Bank Details ---" << endl;
        cout << "Name: " << name << endl;
        cout << "Account Number: " << account_no << endl;
        cout << "Balance: " << balance << endl;
    }

    // Deposit function
    void deposit(float amount) {
        balance += amount;
        cout << "\nAmount Deposited: " << amount << endl;
        cout << "Updated Balance: " << balance << endl;
    }

    // Withdraw function
    void withdraw(float amount) {
        if (amount > balance) {
            cout << "\nInsufficient Balance!" << endl;
        } else {
            balance -= amount;
            cout << "\nAmount Withdrawn: " << amount << endl;
            cout << "Updated Balance: " << balance << endl;
        }
    }
};

int main() {
    BankEmployee emp;

    cin.ignore(); // To handle newline before getline
    emp.getData();
    emp.display();

    float dep, wd;

    cout << "\nEnter amount to deposit: ";
    cin >> dep;
    emp.deposit(dep);

    cout << "\nEnter amount to withdraw: ";
    cin >> wd;
    emp.withdraw(wd);

    return 0;
}