#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *previous;
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    if (*head == NULL)
        *head = new_node;
    else
    {
        current = *head;
        if (current->n >number)
        {
            new_node->next = current;
            *head = new_node;
        }
        else
        {
            while (current != NULL)
            {
                previous = current;
                current = current->next;
                if (current->next == NULL)
                {
                    add_nodeint_end(head, number);
                    break;
                }
                if (current->n > number)
                {
                    previous->next = new_node;
                    new_node->next = current;
                    break;
                }   
            }
        }
    }
    return (new_node);
}