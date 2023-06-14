# Challenge Title

Write a function called validate brackets
Arguments: string
Return: boolean

- representing whether or not the brackets in the string are balanced

#### There are 3 types of brackets:

- Round Brackets : ()
- Square Brackets : []
- Curly Brackets : {}

## Whiteboard Process

![ white board](<../code_challenge13(stack_queue_brackets)/assets/stack_queue_brackets.jpg>)

## Approach & Efficiency

#### **Approach:**

The approach uses a stack to keep track of the opening brackets encountered and ensures that each closing bracket matches the corresponding opening bracket. If any error conditions are encountered during the process, such as unmatched or mismatched brackets, the function prints an error message and returns False.

#### **Big O:**

- Space Complexity: O(n)
- Time Complexity: O(n)

## Solution

![Solution](<../code_challenge13(stack_queue_brackets)/assets/run_stack_queue_brackets.png>)
