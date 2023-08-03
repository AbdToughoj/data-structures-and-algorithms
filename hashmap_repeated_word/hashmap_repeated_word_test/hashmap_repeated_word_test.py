from hashmap_repeated_word.hashmap_repeated_word import hashmapRepeatedWord

def test_hashmapRepeatedWord_case1():
    paragraph = "Once upon a time, there was a brave princess who..."
    expected_output = "a"

    result = hashmapRepeatedWord(paragraph)
    assert result == expected_output

def test_hashmapRepeatedWord_case2():
    paragraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected_output = "it"
    result = hashmapRepeatedWord(paragraph)
    assert result == expected_output

def test_hashmapRepeatedWord_case3():
    paragraph = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    expected_output = "summer"
    result = hashmapRepeatedWord(paragraph)
    assert result == expected_output