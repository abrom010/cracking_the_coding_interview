'''
Given an image represented by an N X N matrix, where each pixel in the image is
represented by an integer, write a method to rotate the image by 90 degrees. Can
you do this in place?

'''

import random

def rotate_matrix(matrix):
	N = len(matrix)

	# transpose
	for i in range(N):
		for j in range(i,N):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp

	# flip horizontally
	for i in range(N):
		for j in range(N):
			temp = matrix[i][j]
			matrix[i][j] = matrix[i][N - 1 - j]
			matrix[i][N - 1 - j] = temp


def main():
	N = 5
	matrix = [[random.randint(0,10) for i in range(N)] for i in range(N)]
	print(matrix)
	rotate_matrix(matrix)
	print(matrix)

if __name__ == "__main__":
	main()