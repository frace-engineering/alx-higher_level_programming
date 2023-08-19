#include "lists.h"



listint_t *rev(listint_t *h);

/**
 * is_palindrome checks if a list is palindrome
 * @head: points to the head node
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr, *prev, *new_head, *brk;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	curr = prev = *head;

	while(curr && curr->next)
	{
		curr = curr->next->next;
		if (curr == NULL)
		{
			new_head = prev->next;
			break;
		}
		if (curr->next == NULL)
		{
			new_head = prev->next->next;
			break;
		}
		prev = prev->next;
	}
	prev->next = NULL;
	new_head = rev(new_head);
	brk = *head;
	while (brk)
	{
		if (brk->n != new_head->n)
			return (0);

		brk = brk->next;
		new_head = new_head->next;
	}
	return (1);
}

/**
 * rev - reverse linked list
 * @h: points to head node
 *
 * Return: rev
 */
listint_t *rev(listint_t *h)
{
	listint_t *curr, *prev, *temp;

	curr = prev = h;

	while (curr != NULL)
	{
		temp = curr->next;
		curr->next = prev;
		prev = curr;
		curr = temp;
	}
	return (prev);
}



