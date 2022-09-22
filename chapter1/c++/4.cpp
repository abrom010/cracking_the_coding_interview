/*
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.

	EXAMPLE

	Input: Tact Coa
	Output: True (permutations: "taco cat", "atco cta", etc.)
*/

#include <bits/stdc++.h>
using namespace std;

bool isPermutationOfPalindrome(string str) {
	string strNoSpace;
	for(int i=0; i<str.size(); i++) {
		if(str[i]!=' ') strNoSpace += (char)tolower(str[i]);
	}

	map<char,int> m;
	for(int i=0; i<strNoSpace.size(); i++) {
		if(m.find(strNoSpace[i])==m.end()) {
			m.insert(make_pair(strNoSpace[i], 1));
		} else {
			m[strNoSpace[i]]++;
		}
	}
	
	bool odd = strNoSpace.size()%2!=0;
	bool encountered_solo = false;
	map<char,int>::iterator itr;
	for(itr = m.begin(); itr != m.end(); itr++) {
		if(itr->second%2!=0) {
			if(odd) {
				if(encountered_solo) return false;
				else encountered_solo = true;
			} else
				return false;
		}
	}
	return true;
}

int main() {
	cout << isPermutationOfPalindrome("Tact Coan");
}
