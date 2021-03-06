//#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	double gallons, charge = 0, total; // Initialize variables
	const int fee = 15;
	double costUpTo6K = 2.35,
		costUpTo20K = 3.75,
		costOver20K = 6.00;

	cout << "Enter the total number of gallons used, divided by 1000: "; // Prompt user for input
	cin >> gallons;

	if (gallons > 20){ // If gallons entered are above 20
		charge = (gallons - 20) * costOver20K;
		charge = charge + (14 * costUpTo20K); 
		charge = charge + (6 * costUpTo6K);
	}
	else if (gallons > 6 && gallons <= 20){ // If gallons entered are above 6 but below 20
		charge = (gallons - 6) * costUpTo20K; 
		charge = charge + (6 * costUpTo6K);
	}
	else { // If gallons are below 6 or equal to 6
		charge = gallons * costUpTo6K; 
	}

	total = charge + fee; // Add calculated charge to the fee
	cout << "You have used " << gallons << " thousand gallons of water." << endl;
	cout << "Your total water bill is $" << setprecision(2) << fixed << total; 

	return 0;
}







