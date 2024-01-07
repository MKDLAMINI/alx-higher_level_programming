#include "lists.h"

/**
 * inverse_listint - takes a linked list and reverses it
 * @head: a pointer to a node of the list
 * Return: return the head
 */
void inverse_listint(listint_t **head)
{
	listint_t *last = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = last;
		last = current;
		current = next;
	}
	*head = last;
}
/**
 * is_palindrome - evaluates if linked list is a palindrome
 * @head: double pointer value to linked list
 * Return: 1 if it is a palindrome, otherwise return 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *blank = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			blank = slow->next;
			break;
		}
		if (!fast->next)
		{
			blank = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	inverse_listint(&blank);

	while (blank && temp)
	{
		if (temp->n == blank->n)
		{
			blank = blank->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!blank)
		return (1);
	return (0);
}
