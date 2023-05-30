from stack_and_queue.stack_and_queue import Stack, Queue 

def test_stack_push():
    stack = Stack()
    stack.push(10)
    actual = stack.peek()
    expected = 10
    assert actual == expected

def test_stack_multiple_push():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    actual = stack.peek()
    expected = 30
    assert actual == expected

def test_stack_pop():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    popped_value = stack.pop()
    actual = popped_value, stack.peek()
    expected = (20, 10)
    assert actual == expected

def test_stack_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_stack_peek_empty():
    stack = Stack()
    try:
        stack.peek()
    except Exception as e:
        actual = str(e)
        expected = "Stack is empty"
        assert actual == expected
    else:
        assert False, "Exception not raised"

def test_stack_instantiation():
    stack = Stack()
    assert stack.is_empty()

def test_stack_pop_empty():
    stack = Stack()
    try:
        stack.pop()
    except Exception as e:
        actual = str(e)
        expected = "Stack is empty"
        assert actual == expected
    else:
        assert False, "Exception not raised"

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(10)
    actual = queue.peek()
    expected = 10
    assert actual == expected

def test_queue_multiple_enqueue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    actual = queue.peek()
    expected = 10
    assert actual == expected

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    dequeued_value = queue.dequeue()
    actual = dequeued_value, queue.peek()
    expected = (10, 20)
    assert actual == expected

def test_queue_peek():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    actual = queue.peek()
    expected = 10
    assert actual == expected

def test_queue_empty():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_queue_peek_empty():
    queue = Queue()
    try:
        queue.peek()
    except Exception as e:
        actual = str(e)
        expected = "Queue is empty"
        assert actual == expected
    else:
        assert False, "Exception not raised"

def test_queue_dequeue_empty():
    queue = Queue()
    try:
        queue.dequeue()
    except Exception as e:
        actual = str(e)
        expected = "Queue is empty"
        assert actual == expected
    else:
        assert False, "Exception not raised"
