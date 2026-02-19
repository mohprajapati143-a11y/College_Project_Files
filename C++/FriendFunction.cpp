#include <iostream>
using namespace std;

class Complex {
    float real, imag;

public:
    void getData() {
        cout << "Enter real part: ";
        cin >> real;
        cout << "Enter imaginary part: ";
        cin >> imag;
    }

    void showData() {
        cout << real << " + j" << imag;
    }

    friend Complex sum(Complex, Complex);
};

Complex sum(Complex c1, Complex c2) {
    Complex c3;
    c3.real = c1.real + c2.real;
    c3.imag = c1.imag + c2.imag;
    return c3;
}

int main() {
    Complex obj1, obj2, obj3;
    cout << "Enter data for 1st complex number:\n";
    obj1.getData();
    cout << "Enter data for 2nd complex number:\n";
    obj2.getData();

    obj3 = sum(obj1, obj2);

    cout << "\nComplex Number 1: "; obj1.showData();
    cout << "\nComplex Number 2: "; obj2.showData();
    cout << "\nSum: "; obj3.showData();
    return 0;
}