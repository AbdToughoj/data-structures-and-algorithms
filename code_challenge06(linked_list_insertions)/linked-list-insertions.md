# Challenge Title

Write the following methods for the Linked List class:

1. **Append:**

- arguments: new value
- method description: adds a new node with the given  value to the end of the list

2. **Insert before:**

- arguments: value, new value
- method description: adds a new node with the given new value immediately before the first node that has the value specified

3. **Insert after:**

- arguments: value, new value
- method description: adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

![ white board](<../code_challenge06(linked_list_insertions)/assets/append_method.jpg>)
![ white board](<../code_challenge06(linked_list_insertions)/assets/insert_before_method.jpg>)
![ white board](<../code_challenge06(linked_list_insertions)/assets/insert_after_method.jpg>)

## Approach & Efficiency

### 1. **Append:**

Approach:
create a new node with the given value. If the linked list is empty, set the new node as the head. Otherwise, traverse the linked list from the head to the last node. Set the "next" attribute of the current node to point to the new node. Finally, update the new node's "next" attribute to None, indicating it is the new last node.

Big O:

- Space Complexity: O(n)
- Time Complexity: O(n)

### 2. **Insert before:**

Approach:
Create a new node with the given new value. If the linked list is empty, set the new node as the head of the linked list. Otherwise, traverse the linked list starting from the head until finding the node that has the value specified. Set the "next" attribute of the new node to point to the node found in the previous step. If the node found is the head, update the head to point to the new node. Otherwise, update the "next" attribute of the previous node to point to the new node. This inserts the new node immediately before the specified node in the linked list.

Big O:

- Space Complexity: O(n)
- Time Complexity: O(n)

### 3. **Insert after:**

Approach:
Create a new node with the given new value. If the linked list is empty, set the new node as the head of the linked list. Otherwise, traverse the linked list starting from the head until finding the node that has the value specified. Set the "next" attribute of the new node to point to the next node of the found node. Update the "next" attribute of the found node to point to the new node. This inserts the new node immediately after the specified node in the linked list.

Big O:

- Space Complexity: O(n)
- Time Complexity: O(n)

## Solution

![ white board](<../code_challenge06(linked_list_insertions)/assets/run.png>)
