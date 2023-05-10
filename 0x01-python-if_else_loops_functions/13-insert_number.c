#include "lists.h"

/**
 * insert_node - inserts a new number at a given position.
 * @head: pointer to head of a list.
 * @number: number to insert nodes
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h;
	listint_t *h_prev;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	do
	{
		if (h->n > number)
			break;
		h_prev = h;
		h = h->next;
	}
	while (h != NULL)

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			h_prev->next = new;
	}
	return (new);
}
