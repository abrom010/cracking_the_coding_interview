'''
Implement an algorithm to determine if a
string has all unique characters. What if 
you cannot use additional data structures?

'''

def is_string_unique(str):
	character_set = set()
	for c in str:
		if c in character_set:
			return False
		else:
			character_set.add(c)
	return True


def main():
	print(is_string_unique("herlo"))

if __name__ == "__main__":
	main()