#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * An XOR linked list is a more memory efficient doubly linked list. Instead of 
 * each node holding next and prev fields, it holds a field named both, which is
 * an XOR of the next node and the previous node. Implement an XOR linked list;
 * it has an add(element) which adds the element to the end, and a get(index)
 * which returns the node at index.
 *
 * If using a language that has no pointers (such as Python), you can assume
 * you have access to get_pointer and dereference_pointer functions that converts
 * between nodes and memory addresses.
 */

/* list element for the xor linked list */
struct node;
typedef struct node node_t;

struct node {
    int value;			/* element's value */
    node_t *both;		/* pointer to previous and next element */
};

/* to make it easy, define the linked list here */
node_t *head = NULL;
node_t *tail = NULL;

/* adds an element to the end of the linked list */
void add(node_t* element);

/* gets the element at a specific index in the linked list */
node_t* get(int index);

/* helper to xor addresses to reduce casts in code */
node_t* xor(node_t *a, node_t *b);

int main(int argc, char argv)
{
	printf("****************************\n");
	printf("*** XOR linked list task ***\n");
	printf("****************************\n\n");

	/* fill the list with ten nodes */
	for(int i = 0; i < 10; ++i) {
		node_t *el = malloc(sizeof(node_t));

		if(el == NULL) {
			printf("Error - error allocating new node\n");
			continue;
		}

		el->value = i;
		add(el);
	}

	/* print all node of the list */
	for(int i = 0; i < 10; ++i) {
		node_t* el = get(i);

		if(el == NULL)
			printf("Node not present\n");
		else
			printf("Node %d\n", el->value);
	}

	/* cleanup is ignored for this test ;-) */
	return 0;
}

void add(node_t* element)
{
	if(head == NULL) {
		/* first element is easy */
		element->both = 0x0;
		head = element;
		tail = element;

	} else {
		/* set the both of the new (last) element */
		element->both = xor(tail, 0);

		/* update the both of the current tail by retrieving previous
		 * element and xor it with new element */
		tail->both = xor(element, xor(tail->both, 0));

		/* here's the new tail */
		tail = element;
	}
}

node_t* get(int index)
{
	int idx = 0;

	node_t *curr = head;
	node_t *prev = NULL;
	node_t *next;

	while((idx != index) && (curr != NULL)) {
		next = xor(prev, curr->both);
		prev = curr;
		curr = next;
		idx++;
	}

	return curr;
}

node_t* xor(node_t *a, node_t *b)
{
	return (node_t*)((uintptr_t)a ^ (uintptr_t)b);
}
