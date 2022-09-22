/*
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
*/

#include <bits/stdc++.h>
using namespace std;

bool isOneEditAway(string a, string b) {
	int sizeDifference = abs((int)a.size()-(int)b.size());
	if(sizeDifference>1) return false;

	int i = 0;
	int j = 0;
	bool foundDiscrepancy = false;
	while(i<a.size() && j<b.size()) {
		if(a[i]!=b[j]) {
			if(sizeDifference==0) {
				if(foundDiscrepancy) {
					return false;
				} else {
					foundDiscrepancy = true;
				}
			} else {
				if(foundDiscrepancy) {
					return false;
				} else {
					if(a.size()>b.size()) i++;
					else j++;
					foundDiscrepancy = true;
				}
			}
		}
		i++;
		j++;
	}
	return true;
}


int main() {
	cout << (isOneEditAway("aabrdjaad", "aabrdkjaad") ? "TRUE" : "FALSE") << endl;
}
