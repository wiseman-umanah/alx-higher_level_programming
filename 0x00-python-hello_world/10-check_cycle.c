#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: the head pointer to list
* Return: 0 if there's no cycle, 1 if found
*/

int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *test;

	int n;

	test = temp = list;
	n = 0;
	while (test != NULL)
	{
		while (temp != NULL)
		{
			temp = temp->next;
			if (temp == test)
			{
				n = 1;
				break;
			}
		}
		test = test->next;
		temp = list;
	}
	return (n);
}
