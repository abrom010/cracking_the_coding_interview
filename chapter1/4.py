'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need
to be limited to just dictionary words. You can ignore casing and non-letter characters.

	EXAMPLE

	Input: Tact Coa
	Output: True (permutations: "taco cat", "atco cta", etc.)

'''
def is_permutation_of_palindrome(str: str):
	str = str.lower()
	c_set = dict()

	for c in str:
		if c in c_set:
			c_set[c] += 1
		else:
			c_set.update({c: 1})

	odd = len(str)%2==0
	encountered_solo = False
	#del c_set[' ']
	for key in c_set:
		if key == ' ':
			continue
		if c_set[key]%2 != 0:
			if odd:
				if encountered_solo:
					return False
				else:
					encountered_solo = True
			else:
				return False
	return True


def main():
	print(is_permutation_of_palindrome("Tact Coa"))

if __name__ == "__main__":
	main()