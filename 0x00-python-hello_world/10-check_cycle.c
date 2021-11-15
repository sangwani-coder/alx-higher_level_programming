#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 *check_cycle - check if linked list has a cycle in it
 *@list: value check
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list, *y = list;

	if (list == NULL)
		return (0);

	while (y && y->next)
	{
		y = y->next->next;
		x = x->next
		if (x == y)
			return (1);
	}
	return (0);
}
