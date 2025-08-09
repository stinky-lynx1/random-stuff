#include <iostream>
#include <ctime>
#include <unistd.h>

int main() {
	int h = 0, m = 0, s = 0, prevS = -1;
    const int div = 60;
    std::string a = "", b = "", c = "", time;
	time_t start = ::time(nullptr), now;

	while (true){
        prevS = s;
		s = ::time(nullptr) - start;
        usleep(50000);
		if (s >= div){
			s = 0;
			m++;
			if (m >= div){
				m = 0;
				h++;
			}
            start = ::time(nullptr);
		}
        if (prevS != s){
            a = (h < 10) ? "0" : "", b = (m < 10) ? ":0" : ":", c = (s < 10) ? ":0" : ":";
            std::string sh = std::to_string(h), sm = std::to_string(m), ss = std::to_string(s);
            time = a + sh + b + sm + c + ss;
            std::cout << "\r" << time;
            std::cout.flush();
        }
        if (h == 23 && m == 59 && s == 59) {
            std::cout << " (stopped)\nTime limit reached!";
            return 0;
		}
	}
}
