'''
Write an algorithm such that if an element in an M X N matrix is 0,
its entire row and column are set to 0.

'''
import random
from pprint import pprint

N = 5
matrix = [[random.randint(0,10) for i in range(N)] for i in range(N)]
pprint(matrix)


''' easy solution, just store the values of rows and columns that should be converted '''
# conversion_list = []
# for i in range(N):
# 	for j in range(N):
# 		if matrix[i][j] == 0:
# 			conversion_list.append((i,j))

# for i,j in conversion_list:
# 	for b in range(N):
# 		matrix[i][b] = 0
# 	for a in range(N):
# 		matrix[a][j] = 0
# print()
# pprint(matrix)

''' improving on this solution, uniquely store each row and column '''
row_set = set()
column_set = set()

for i in range(N):
	for j in range(N):
		if matrix[i][j] == 0:
			if i not in row_set:
				row_set.add(i)
			if j not in column_set:
				column_set.add(j)

for i in row_set:
	for j in range(N):
		matrix[i][j] = 0

for j in column_set:
	for i in range(N):
		matrix[i][j] = 0
		
print()
pprint(matrix)
