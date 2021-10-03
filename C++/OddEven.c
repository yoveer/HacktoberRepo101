#include "calculator.h"
#include<iostream>
using namespace std;

void calculator::setValue(int s, int e)
{
	x = s;
	y = e;

}

void calculator::calculate()
{
	if (x < 0) {
		cout << "You entered minus value " << endl;
	}
		

	else if(x>y) {
		cout << "check your entered number " << endl;

	}

	else {
		int even=0, odd=0;
		for (int i = x; i <= y; i++) {

			if (i % 2 == 0) {
				even += i;
				e = even;

			}
			else if(i%2==1){
				odd += i;
				o = odd;
			}
		}
	}
}

void calculator::display()
{
	calculate();

	if (x < y && x>0 && y > 0) {

		cout << "----------------------------------------------------------" << endl;
		cout << " " << x << "  to  " << y << " odd number sum is : " << o << endl;
		cout << " " << x << "  to  " << y << " even number sum is : " << e << endl;
		cout << "----------------------------------------------------------" << endl;
	}

	else {
		cout << "---sorry you entered wrong value---" << endl;

	}
}
