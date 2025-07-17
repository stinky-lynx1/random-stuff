#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <functional>

using namespace std;

	auto calc = [](double x)
	{
    	return pow(x, 2);           // <- INSERT YOUR FUNCTION IN THIS LINE
	};

int main()
{
	double x2;
	double x1;
	double dx;
    double y;
    double i;

    cout << "High a="; cin >> x2;
    cout << endl << "Low b="; cin >> x1;
    cout << endl << "Variable dx="; cin >> dx;
    
    while (x1 < x2)
    {
        y = calc(x1);
        i += y * dx;
        x1 += dx;
    }

    cout << "Integral is " << i << endl;
}