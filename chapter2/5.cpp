/*
You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1's
digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list. (You are not allowed to "cheat" and just
convert the linked list to an integer.)

EXAMPLE

Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP

Supposed the digits are stored in forward order. Repeat the above problem.

EXAMPLE

Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
*/

// INCOMPLETE

#include <bits/stdc++.h>
using namespace std;

class Node {
public:
	int data;
	Node* next;

	Node() : data(0), next(NULL) {}

	Node(int value) : data(value), next(NULL) {}
};

ostream& operator<<(ostream &out, const Node* node) {
	out << node->data;
	while (node->next != NULL) {
		out << " -> ";
		node = node->next;
		out << node->data;
	}
	return out;
}

Node* AddNumbers(Node* head1, Node* head2) {
	Node* head3 = new Node();

	Node* current1 = head1;
	Node* current2 = head2;
	Node* current3 = head3;

	Node* secondToLast;

	bool carry = false;
	while(current1!=NULL && current2!=NULL) {
		int sum = current1->data + current2->data;

		if(carry) {
			int totalSum = sum + 1;
			// need to carry again
			if(totalSum>9) {
				current3->data = totalSum%10;
			} else {
				carry = false;
				current3->data = totalSum;
			}
		} else {
			// need to carry
			if(sum>9) {
				carry = true;
				current3->data = sum%10;
			} else {
				current3->data = sum;
			}
		}

		current3->next = new Node();
		secondToLast = current3;
		current3 = current3->next;

		current1 = current1->next;
		current2 = current2->next;
		
	}

	while(current1!=NULL) {

	}

	while(current2!=NULL) {

	}

	return head3;
}

int main() {
	Node* head1 = new Node();
	Node* head2 = new Node();
	
	srand(time(NULL));

	Node* current1 = head1;
	Node* current2 = head2;
	for(int i=0; i<10; i++) {
		current1->data = (rand()%10);
		current2->data = (rand()%10);
		current1->next = new Node();
		current2->next = new Node();
		current1 = current1->next;
		current2 = current2->next;
	}

	cout << head1 << endl;
	cout << head2 << endl;
	Node* head3 = AddNumbers(head1, head2);
	cout << head3 << endl;
}