#include <bits/stdc++.h>
using namespace std;

bool isPermutation(string a, string b) {
	if(a.size()!=b.size()) return false;
	map<char, int> a_map;
	map<char, int> b_map;

	for(int i=0; i<a.size(); i++) {
		if(a_map.find(a[i])!=a_map.end()) {
			a_map[a[i]]++;
		} else {
			a_map[a[i]] = 1;
		}
		if(b_map.find(b[i])!=b_map.end()) {
			b_map[a[i]]++;
		} else {
			b_map[a[i]] = 1;
		}
	}
	
	if(a_map.size() != b_map.size()) return false;
	map<char,int>::iterator itr;
	for(itr = a_map.begin(); itr!=a_map.end(); itr++) {
		if(itr->second!=b_map[itr->first]) return false;
	}

	return true;
}

int main() {
	cout << isPermutation("hello", "lehlo") << endl;	
}
