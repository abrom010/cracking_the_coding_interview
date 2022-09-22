'''
Assume you have a method isSubstring which checks if one word is a substring of another. Given
two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

'''

def is_substring(s1,s2):
	if len(s1) == len(s2):
		return False
	elif len(s1) > len(s2):
		i = 0
		j = len(s2)
		for n in range(len(s1)-j+1):
			if s2 == s1[i:j]:
				return True
			i += 1
			j += 1
	else:
		i = 0
		j = len(s1)
		for n in range(len(s2)-j+1):
			if s1 == s2[i:j]:
				return True
			i += 1
			j += 1

	return False

def is_rotation(s1,s2):
	# s2 will be substring of s1s1
	if len(s1) == len(s2) and len(s1) > 0:
		s1s1 = s1+s1
		return is_substring(s1s1, s2)



if __name__ == "__main__":
	s1 = "waterbottle"
	s2 = "erbottlewat"

	print(is_rotation(s1,s2))


	
	