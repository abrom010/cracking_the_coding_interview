/*
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please us a character array so that you can perform this operation in place.
 
	EXAMPLE
 	
 	Input: "Mr John Smith    ", 13
 	Output: "Mr%20John%20Smith"
 */

#include <bits/stdc++.h>
using namespace std;

string replaceWith20(string str, int trueLength) {
	int i = trueLength - 1;
	int j = str.size() - 1;

	while(i>0) {
		if(str[i]==' ') {
			str[j--] = '0';
			str[j--] = '2';
			str[j--] = '%';
		} else {
			str[j--] = str[i];
		}
		i--;
	}

	return str;
}

int main() {
	cout << replaceWith20("Mr John Smith    ", 13) << endl;
}
