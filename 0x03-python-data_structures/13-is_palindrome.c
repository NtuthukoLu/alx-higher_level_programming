#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head) 
{
    if (head == NULL || *head == NULL) 
    {
        return 1;
    }
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *curr = NULL;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        curr = slow->next;
        slow->next = prev;
        prev = slow;
        slow = curr;
    }
    if (fast != NULL) {
        slow = slow->next;
    }
    while (slow != NULL) {
        if (prev->n != slow->n) {
            return 0;
        }
        prev = prev->next;
        slow = slow->next;
    }
    return 1;
}
