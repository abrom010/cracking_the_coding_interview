'''
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to
hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please us a
character array so that you can perform this operation in place.
 
	EXAMPLE
 	
 	Input: "Mr John Smith    ", 13
 	Output: "Mr%20John%20Smith"

'''
def compress_string(s):
	last_character = None
	character_count = 1
	str2 = ""

	for c in s:
		if last_character == None:
			last_character = c
			str2 += c
		elif last_character==c:
			character_count += 1
		else:
			last_character = c
			str2 += str(character_count)
			character_count = 1
			str2 += c

	return str2

def main():
	print(compress_string("aaabeeffffg"))

if __name__ == "__main__":
	main()