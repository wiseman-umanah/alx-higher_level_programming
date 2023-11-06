#include "lists.h" 

int is_palindrome(listint_t **head)
{
    int ispalindrome, i, temp[1000];
    listint_t *current;
    
    ispalindrome = 1;
    i = 0;
    if (*head == NULL)
        return (i);
    current = *head;
    while (current != NULL)
    {
        temp[i] = current->n;
        current = current->next;
        i++;
    }
    i--;
    current = *head;
    while (i >= 0 && current != NULL)
    {
        if (temp[i] != current->n)
        {
            ispalindrome = 0;
            break;
        }
        i--;
        current = current->next;
    }
    return (ispalindrome);
}