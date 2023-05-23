# Challenge Title

This problem involves implementing a linked list data structure with a Node class and a Linked List class. The Linked List class has a head property and provides methods to insert a new node at the head, check if a value exists in the list, and obtain a string representation of all the values in the list. The goal is to achieve O(1) time complexity for the insert operation by adding new nodes at the head.

## Whiteboard Process

![ white board](<../code_challenge05(linked-list)/assets/linked_list.jpg>)

## Approach & Efficiency

Approach:
The approach is to create a linked list data structure where nodes can be inserted at the head. The code defines a Node class to represent individual nodes with a value and a next pointer. The LinkedList class has a head property representing the first node. The insert method creates a new node, and if the list is empty, it becomes the head; otherwise, it is inserted at the head by updating pointers.

Big O:

- Space Complexity: O(1)
- Time Complexity: O(1)

## Solution

![ white board](<../code_challenge05(linked-list)/assets/linked_list_run.png>)
