from hashmap_left_join.hashmap_left_join import left_join, HashTable

def test_hashmap_left_join_one():
    ht1 = HashTable()
    ht2 = HashTable()

    ht1.set('diligent', 'employed')
    ht1.set('fond','enamored')
    ht1.set('guide', 'usher')  
    ht1.set('outfit', 'garb')
    ht1.set('wrath', 'anger')

    ht2.set('diligent', 'idle')
    ht2.set('fond', 'averse')
    ht2.set('guide', 'follow')  
    ht2.set('flow', 'jam')
    ht2.set('wrath', 'delight')

    result = left_join(ht1, ht2)

    expected_output = [
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'], 
        ['outfit', 'garb', None],
        ['wrath', 'anger', 'delight'],
    ]

    assert result == expected_output

[
      ['diligent', 'employed', 'idle'],
      ['guide', 'usher', 'follow'], 
      ['guide', 'usher', 'follow'], 
      ['outfit', 'garb', None], 
      ['wrath', 'anger', 'delight']
]

def test_hashmap_left_join_two():
    ht1 = HashTable()
    ht2 = HashTable()

    ht1.set('apple', 'red')
    ht1.set('banana', 'yellow')
    ht1.set('cherry', 'red')
    ht1.set('date', 'brown')
    ht1.set('elderberry', 'purple')

    ht2.set('apple', 'green')
    ht2.set('cherry', 'black')
    ht2.set('grape', 'purple')
    ht2.set('kiwi', 'brown')
    ht2.set('lemon', 'yellow')

    result = left_join(ht1, ht2)

    expected_output = [
        ['apple', 'red', 'green'],
        ['banana', 'yellow', None],
        ['cherry', 'red', 'black'],  
        ['date', 'brown', None],
        ['elderberry', 'purple', None],
    ]

    assert result == expected_output


def test_hashmap_left_join_three():
    ht1 = HashTable()
    ht2 = HashTable()

    ht1.set('cat', 'meow')
    ht1.set('dog', 'woof')
    ht1.set('elephant', 'trumpet')
    ht1.set('giraffe', 'neck')
    ht1.set('horse', 'neigh')

    ht2.set('cat', 'purr')
    ht2.set('dog', 'bark')
    ht2.set('lion', 'roar')
    ht2.set('giraffe', 'spots')
    ht2.set('kangaroo', 'hop')

    result = left_join(ht1, ht2)

    expected_output = [
        ['cat', 'meow', 'purr'],
        ['dog', 'woof', 'bark'],
        ['elephant', 'trumpet', None],
        ['giraffe', 'neck', 'spots'],  
        ['horse', 'neigh', None],
    ]

    assert result == expected_output



