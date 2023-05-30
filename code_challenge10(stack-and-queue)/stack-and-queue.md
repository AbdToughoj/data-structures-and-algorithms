# Challenge Title

#### Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue:

#### **Node:**

- #### Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

#### **Stack:**

- #### Create a Stack class that has a top property. It creates an empty Stack when instantiated.

  - This object should be aware of a default empty value assigned to top when the stack is created.
  - The class should contain the following methods:
  - push

    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.

  - pop

    - Arguments: none
    - Returns: the value from node from the top of the stack
      \*Removes the node from the top of the stack
    - Should raise exception when called on empty stack

  - peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.

#### **Queue:**

- #### Create a Queue class that has a front property. It creates an empty Queue when instantiated.
  - This object should be aware of a default empty value assigned to front when the queue is created.
  - The class should contain the following methods:
  - enqueue
    - Arguments: value
    - adds a new node with that value to the back of the queue with an O(1) Time performance.
  - dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
  - peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty

## Approach & Efficiency

### Stack Approach:

- push: Create a new node with the given value and set it as the new top of the stack.
- pop: Remove and return the value of the top element of the stack.
- peek: Return the value of the top element of the stack without removing it.
- is_empty: Check if the stack is empty by verifying if the top is None.

### Queue Approach:

- enqueue: Create a new node with the given value and set it as the new rear of the queue.
- dequeue: Remove and return the value of the front element of the queue.
- peek: Return the value of the front element of the queue without removing it.
- is_empty: Check if the queue is empty by verifying if the front is None.

### Stack Big O:

#### push:

- Time Complexity: O(1)
- Space Complexity: O(1)

#### pop:

- Time Complexity: O(1)
- Space Complexity: O(1)

#### peek:

- Time Complexity: O(1)
- Space Complexity: O(1)

#### is_empty:

- Time Complexity: O(1)
- Space Complexity: O(1)

### Queue Big O:

#### enqueue:

- Time Complexity: O(1)
- Space Complexity: O(1)

#### dequeue:

- Time Complexity: O(1)
- Space Complexity: O(1)

#### peek:

- Time Complexity: O(1)
- Space Complexity: O(1)

#### is_empty:

- Time Complexity: O(1)
- Space Complexity: O(1)

## Solution

![Solution](<../code_challenge10(stack-and-queue)/assets/stack_and_queue.png>)
