#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - function stores singly linked list
 * @n: integer value
 * @next: points to the next node
 * Description: This is the structure that stores singly linked lists
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t **head, int number);

#endif /*LISTS_H*/

