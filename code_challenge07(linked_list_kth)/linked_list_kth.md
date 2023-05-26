# Challenge Title

#### Write the following method for the Linked List class:

**kth from end:**

- argument: a number, k, as a parameter.
- Return the node’s value that is k places from the tail of the  linked list.
- You have access to the Node class and all the properties on  the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

![ white board](<../code_challenge07(linked_list_kth)/assets/linked_list_kth.jpg>)

## Approach & Efficiency

#### **Approach**:

To find the kth node from the end in a linked list, check if the list is empty or if k is negative. Traverse the list to count the nodes, and return "Exception" if k exceeds the count. Reset the current node to the head, iterate (count - k - 1) times, and update the current node. Return the value of the current node as the kth node from the end. This algorithm handles exceptions and efficiently retrieves the desired node.

#### **Big O:**

- Space Complexity: O(1)
- Time Complexity: O(n)

## Solution

![ white board](<../code_challenge07(linked_list_kth)/assets/test_linked_list_kth.png>)
