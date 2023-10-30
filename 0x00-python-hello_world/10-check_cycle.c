#include "lists.h"

/**
 * check_cycle - checks if the link list contains cycle
 * @list: link list to check
 *
 * Return: 1 if list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *perm = list;
	listint_t *test = list;

	if (!list)
		return (0);

	while (perm && test && test->next)
	{
		perm = perm->next;
		test = test->next->next;
		if (perm == test)
			return (1);
	}

	return (0);
}
