#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: the head pointer to list
* Return: 0 if there's no cycle, 1 if found
*/

int check_cycle(listint_t *list)
{
	listint_t *temp;
	int n;

	temp = list;
	n = 0;
	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == list)
		{
			n = 1;
			break;
		}
	}
	return (n);
}
