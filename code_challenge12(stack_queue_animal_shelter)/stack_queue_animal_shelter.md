# Challenge Title

- Create a new class called pseudo queue.
  - Do not use an existing Queue.
  - Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
  - Internally, utilize 2 Stack instances to create and manage the queue
- Methods:
  - enqueue
    - Arguments: value
    - Inserts a value into the PseudoQueue, using a first-in, first-out approach.
  - dequeue
    - Arguments: none
    - Extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Whiteboard Process

## Approach & Efficiency

#### **approach:**

The AnimalShelter class maintains separate queues for dogs and cats, adhering to a first-in, first-out approach. In this approach, animals are enqueued into their respective queues based on their species using the enqueue method. The dequeue method allows retrieval of the first animal from the requested queue, either for dogs or cats, according to the preference provided. If an invalid preference is given or the requested queue is empty, the method returns None. It's worth noting that the enqueue operation is efficient, while the performance of the dequeue operation may vary depending on the number of animals in the queues.

#### **Big O:**

enqueue method:

- Space Complexity: O(1)
- Time complexity : O(1)

dequeue method:

- Space Complexity: O(n)
- Time complexity : O(1)

## Solution

![Solution](<../code_challenge12(stack_queue_animal_shelter)/assets/run_stack_queue_animal_shelter.png>)
