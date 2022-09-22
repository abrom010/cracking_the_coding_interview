'''
Implement an algorithm to find the kth to last element of a singly linked list.

'''

import random

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self, head_value):
		self.head = Node(head_value)

	def append(self, value):
		current_node = self.head
		while(current_node.next != None):
			current_node = current_node.next
		current_node.next = Node(value)

	def print(self):
		current_node = self.head
		print("[ ", end="")
		while current_node != None:
			print(str(current_node.value), end=" ")
			current_node = current_node.next
		print("]")

# my original easy solution
def kth_to_last_element(linked_list, k):
	current_node = linked_list.head
	size = 0
	if current_node == None:
		return None
	while current_node != None:
		size += 1
		current_node = current_node.next

	current_node = linked_list.head
	for i in range(size-k):
		current_node = current_node.next

	return current_node.value

# fav solution
def kth_to_last_element_better(linked_list, k):
	j = linked_list.head
	for i in range(k):
		j = j.next
	i = linked_list.head
	while j != None:
		i = i.next
		j = j.next
	return i.value

# there were also a few recursive solutions

def main():
	linked_list = LinkedList(random.randint(0,10))
	for i in range(10):
		linked_list.append(random.randint(0,10))

	linked_list.print()
	print(kth_to_last_element(linked_list, 4))
	print(kth_to_last_element_better(linked_list, 4))

if __name__ == "__main__":
	main()
