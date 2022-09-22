'''
Write code to remove duplicates from an unsorted linked list.

FOLLOW UP

How would you solve this problem if a temporary buffer is not allowed?

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

# save values to set, traverse linked list and remove if node if value already in set
# this is messy :/
def remove_duplicates(linked_list):
	node_a = linked_list.head
	if node_a.next == None: return
	value_set = set()
	value_set.add(node_a.value)
	print("added: " + str(node_a.value))
	node_b = node_a.next
	if node_b.value == node_a.value:
		node_a.next = node_b.next
		print("removed: " + str(node_b.value))
	else:
		value_set.add(node_b.value)
		print("added: " + str(node_b.value))
	if node_b.next != None:
		node_a = node_b
		node_b = node_b.next
	while node_b.next != None:
		if node_b.value in value_set:
			print("removed: " + str(node_b.value))
			node_a.next = node_b.next
			node_b = node_b.next
		else:
			value_set.add(node_b.value)
			print("added: " + str(node_b.value))
			node_a = node_b
			node_b = node_b.next

# brute force? yep. just stop at each node k and traverse k..n, removing nodes with same value
def remove_duplicates_no_buffer(linked_list):
	pass

def main():
	linked_list = LinkedList(random.randint(0,10))
	for i in range(10):
		linked_list.append(random.randint(0,10))
	linked_list.print()
	remove_duplicates(linked_list)
	linked_list.print()

if __name__ == "__main__":
	main()