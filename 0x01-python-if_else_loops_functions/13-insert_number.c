#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly-linked list.
 * @head: a pointer to the head of linked list
 * @number: a number to be inserted
 *
 * Return: address of the new node NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

        current = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->next->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current_next = new_node;
	return (new_node);
}
