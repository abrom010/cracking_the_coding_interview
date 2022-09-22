/*
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
*/

#include <bits/stdc++.h>
using namespace std;

string compressString(string str) {
	char lastCharacter = '\0';
	int characterCount = 1;
	string str2 = "";

	for(int i=0; i<str.size(); i++) {
		if(lastCharacter=='\0') {
			lastCharacter = str[i];
			str2 += str[i];
		} else if(lastCharacter==str[i]) {
			characterCount++;
		} else {
			lastCharacter = str[i];
			str2 += to_string(characterCount);
			characterCount = 1;
			str2 += str[i];
		}
	}
	return str2;
}

int main() {
	cout << compressString("aaabeeffffg") << endl;
}
