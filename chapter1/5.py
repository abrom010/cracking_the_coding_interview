'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to
check if they are one edit (or zero edits) away.

'''
def is_one_edit_away(a,b):
	size_difference = abs(len(a)-len(b))
	if(size_difference>1): return False

	i = 0
	j = 0
	found_discrepancy = False
	while(i<len(a) and j<len(b)):
		if a[i]!=b[j]:
			if size_difference == 0:
				if found_discrepancy:
					return False
				else:
					found_discrepancy = True
			else:
				if found_discrepancy:
					return False
				else:
					if(len(a)>len(b)):
						i += 1
					else:
						j += 1
						found_discrepancy = True
		i += 1
		j += 1

	return True

def main():
	print(is_one_edit_away("aba", "aaa"))

if __name__ == "__main__":
	main()