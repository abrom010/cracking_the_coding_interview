/*
 * Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
 * structures?
 */
#include <bits/stdc++.h>
using namespace std;

bool isStringUnique(string s) {
	set<char> charset;
	for(int i=0; i<s.size(); i++) {
		if(charset.find(s[i])!=charset.end())
			return false;
		else
			charset.insert(s[i]);
	}
	return true;
}

bool isStringUniqueNoAdditionalDataStructures(string s) {
	for(int i=0; i<s.size(); i++) {
		for(int j=0; j<s.size(); j++) {
			if(i!=j)
				if(s[i]==s[j]) return false;
		}
	}
	return true;
}

int main() {
	cout << isStringUnique("hello") << endl;
	cout << isStringUniqueNoAdditionalDataStructures("hello") << endl;
}
