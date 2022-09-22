'''
Write code to partition a linked list around a value x, such that all nodes less than x
come before all nodes greater than or equal to x. (IMPORTANT: The partition element
x can appear anywhere in the "right partition"; it does not need to appear
between the left and right partitions. The additional spacing in the example
below indicates the partition. Yes, the output below is one of many valid output!)


EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2     ->      10 -> 5 -> 5 -> 8

'''

import random
from linked_list import LinkedList, Node

# attempting a two pointer method. once you get to the value, both pointers will compare and swap if necessary.
# if no more space in the partition, append a node
# STILL NOT WORKING
def partition(linked_list, x):
	j = linked_list.head
	k = 0 # index of x
	# find k by traversing until we hit the value
	while j.data != x:
		j = j.next
		k += 1

	i = linked_list.head
	index = 0
	while True:
		# both sides aren't traversed yet
		if index < k and j.next != None:
			# left partition member doesn't belong
			if i.data >= x:
				# right partition member doesn't belong
				if j.data < x:
					# swap
					temp = i.data
					i.data = j.data
					j.data = i.data
					# increase both pointers
					i = i.next
					j = j.next
					index += 1
				else:
					# increase right pointer
					j = j.next
			# right partition member doesn't belong
			elif j.data < x:
				i = i.next
				index += 1
			else:
				i = i.next
				j = j.next
				index += 1
		elif index < k:
			# left partition member doesn't belong
			if i.data >= x:
				# store temp data for current node
				temp_data = i.data
				# take next node's data, deleting next node
				i.data = i.next.data
				i.next = i.next.next
				# add node to right partition
				j.next = Node()
				j = j.next
				j.data = temp_data
			else:
				# increase left pointer
				i = i.next
				index += 1
		elif j.next != None:
			# right partition member doesn't belong
			if j.data < x:
				# store temp data for current node
				temp_data = j.data
				# take next node's data, deleting next node
				j.data = j.next.data
				j.next = j.next.next
				# add node to right partition
				temp_next = i.next
				i.next = Node()
				i = i.next
				i.data = j.data
				i.next = temp_next
		else:
			break

# book solution just iterates through the linked list, populating 2 separate linked lists for
# the separate partitions, then joins those at the end

def main():
	linked_list = LinkedList()
	linked_list.head = Node()
	current = linked_list.head
	save_value = 0
	for i in range(10):
		data = random.randint(0,10)
		if i == 5:
			save_value = data
		current.data = data
		current.next = Node()
		current = current.next
	print(linked_list)
	partition(linked_list, save_value)
	print(linked_list)

if __name__ == "__main__":
	main()