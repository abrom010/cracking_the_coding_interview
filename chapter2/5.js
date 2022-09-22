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

function Node() {
	return {
		data: 0,
		next: null,
		print: function () {
			current = this;
			while (current != null) {
				process.stdout.write(current.data + " ");
				current = current.next;
			}
			process.stdout.write("\n");
		},
		populate: function () {
			let current = this;
			current.data = getRandomNumber();
			for (let i = 0; i < 10; i++) {
				current.next = Node();
				current = current.next;
				current.data = getRandomNumber();
			}
		},
	};
}

function getRandomNumber() {
	return Math.round(Math.random() * 10);
}

let head1 = Node();
let head2 = Node();

head1.populate();
head2.populate();

head1.print();
head2.print();

function addNumbers(head1, head2) {
	let carry = false;
	while (head1 != null && head2 != null) {

	}

	while (head1 != null) {

	}

	while (head2 != null) {

	}
}

let head3 = addNumbers(head1, head2);
head3.print();
