'''
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters, and that you are given the "true" length of
the string. (Note: If implementing in Java, please us a character array
so that you can perform this operation in place.
 
	EXAMPLE
 	
 	Input: "Mr John Smith    ", 13
 	Output: "Mr%20John%20Smith"

'''

def replaceWith20(str, trueLength):
	i = trueLength - 1
	j = len(str) - 1

	#pretending string to list doesn't count... strings immutable in python

	str_arr = list(str)
	while(i>0):
		if str_arr[i]==' ':
			str_arr[j] = '0'
			j -= 1
			str_arr[j] = '2'
			j -= 1
			str_arr[j] = '%'
			j -= 1
		else:
			str_arr[j] = str_arr[i]
			j -= 1
		i -= 1

	return ''.join(str_arr)

def main():
	print(replaceWith20("Mr John Smith    ", 13))

if __name__ == "__main__":
	main()