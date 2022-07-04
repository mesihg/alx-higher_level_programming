#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to head of the linked list
 *
 * Return: Reversed linked list
 */
listint_t reverse_listint(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - checks if the given linked list is a palindrome
 * @head: Pointer to head of the linked list
 *
 * Return: 1 it is palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || *head->next == NULL)
		return (1);
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t temp = *head;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow->next = reverse(slow->next);
	slow = slow->next;
	while (slow != NULL)
	{
		if (temp->data != slow->data)
			return (0);
		temp = temp->next;
		slow = slow->next;
	}
	return (1);
}
