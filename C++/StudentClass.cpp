#include <iostream>
using namespace std;

class Student {
    string name;
    int age;
    float percentage;

    void getData() { // private method
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
        cout << "Enter percentage: ";
        cin >> percentage;
    }

public:
    void displayData() {
        getData();
        cout << "\n--- STUDENT INFORMATION ---\n";
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Percentage: " << percentage << endl;
    }
};

int main() {
    Student s;
    s.displayData();
    return 0;
}