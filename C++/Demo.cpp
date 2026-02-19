#include <iostream>
#include <cmath>
using namespace std;

class Demo {
    int n; // User number

public:
    void readNo() {
        cout << "Enter a number: ";
        cin >> n;
    }

    int factorial() {
        int f = 1;
        for (int i = 1; i <= n; i++) f *= i;
        return f;
    }

    int reverseNo() {
        int temp = n, num = 0;
        while (temp > 0) {
            num = num * 10 + temp % 10;
            temp /= 10;
        }
        return num;
    }

    bool isPalindrome() {
        return n == reverseNo();
    }

    bool isArmstrong() {
        int temp = n, sum = 0;
        int digits = 0;
        
        // Count digits
        temp = n;
        while (temp > 0) { temp /= 10; digits++; }
        
        temp = n;
        while (temp > 0) {
            int d = temp % 10;
            sum += pow(d, digits);
            temp /= 10;
        }
        return sum == n;
    }
};

int main() {
    Demo d;
    d.readNo(); // Number read only once

    cout << "\nFactorial = " << d.factorial();
    cout << "\nReverse = " << d.reverseNo();
    cout << "\nPalindrome? " << (d.isPalindrome() ? "Yes" : "No");
    cout << "\nArmstrong? " << (d.isArmstrong() ? "Yes" : "No");
    return 0;
}
