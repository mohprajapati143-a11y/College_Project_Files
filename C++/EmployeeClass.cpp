#include <iostream>
using namespace std;

class Employee {
    string name;
    int age;
    float basic_sal;

    void getInfo() { // private method
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
        cout << "Enter basic salary: ";
        cin >> basic_sal;
    }

public:
    void displayInfo() {
        getInfo();
        cout << "\n--- EMPLOYEE INFORMATION ---\n";
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Basic Salary: " << basic_sal << endl;
        cout << "Gross Salary: " << basic_sal + (0.6 * basic_sal) + (0.4 * basic_sal) << endl;
    }
};

int main() {
    Employee e;
    e.displayInfo();
    return 0;
}