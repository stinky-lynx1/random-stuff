#include <iostream>
#include <ctime>
#include <unistd.h>

using namespace std;

int main() {
	int h = 0, m = 0, s = 0;
    const int div = 60;
    string a = "", b = "", c = "", time;
	clock_t start = clock(), sec;

	while (true){
		sec = clock() - start;
        int prevS = s;
		s = sec / CLOCKS_PER_SEC;
//        usleep(50000);
		if (s % div == 0 && s != 0){
			s = 0;
			m++;
			if (m % div == 0 && m != 0){
				m = 0;
				h++;
			}
            start = clock();
		}
        if (prevS != s){
            a = (h < 10) ? "0" : "", b = (m < 10) ? ":0" : ":", c = (s < 10) ? ":0" : ":";
            string sh = to_string(h), sm = to_string(m), ss = to_string(s);
            time = a + sh + b + sm + c + ss;
            cout << "\r" << time;
            cout.flush();
        }
	}
}