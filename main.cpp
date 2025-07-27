#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <functional>

using namespace std;

int main()
{
    double x2, x, dx, y, i;
    do {
        cout << "High a: ";
        cin >> x2;
        cout << "Low b: ";
        cin >> x;
        cout << "Variable dx: ";
        cin >> dx;
    } while (x >= x2);
    while (x < x2)
    {
        y = pow(x, 2); // <-------------- function goes here (hewp)
        i += y * dx;
        x += dx;
    }

    cout << "Integral is " << i << endl << "boop :3" << endl;
    return 0;
}
