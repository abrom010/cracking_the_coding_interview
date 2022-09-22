'''
Given two strings, write a method to decide
if one is a permutation of the other.

'''
def is_permutation(a,b):
	if len(a) != len(b):
		return False

	character_map = dict()

	for c in a:
		if c in character_map:
			character_map[c] += 1
		else:
			character_map.update({c: 1})

	for c in b:
		if c in character_map:
			character_map[c] -= 1
		else:
			character_map.update({c: -1})
	
	for key in character_map:
		if character_map[key] != 0:
			return False

	return True

def main():
	print(is_permutation("hellko", "klehlo"))

if __name__ == "__main__":
	main()