'''
Implement an algorithm to delete a node in the middle (ie, any node but the first and last node, not necessarily in the exact middle)
of a singly linked list, given only access to that node.

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

# copy next node's data to current node, next node gets garbage collected
def delete_middle_node(node):
	node.value = node.next.value
	#node.next = node.next.next

	temp_next = node.next.next 
	node.next.next = None # note sure if this is necessary, for the gc to pick it up, idk how it works
	node.next = temp_next

def main():
	linked_list = LinkedList(random.randint(0,10))
	for i in range(10):
		linked_list.append(random.randint(0,10))

	linked_list.print()

	current_node = linked_list.head
	k = 4
	for i in range(4):
		current_node = current_node.next
	print(delete_middle_node(current_node))

	linked_list.print()
	

if __name__ == "__main__":
	main()