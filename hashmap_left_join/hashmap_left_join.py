def handle_null_value(value):
    return value if value is not None else 'NULL'


def left_join(synonyms, antonyms):
    result = []

    for key, synonym in synonyms.items():
        antonym = antonyms.get(key, None)
        result.append([key, synonym, handle_null_value(antonym)])

    return result


# Test cases
if __name__ == "__main__":
    synonyms1 = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher',
        'outfit': 'garb',
        'wrath': 'anger'
    }
    antonyms1 = {
        'diligent': 'idle',
        'fond': 'averse',
        'guide': 'follow',
        'flow': 'jam'
    }
    result1 = left_join(synonyms1, antonyms1)
    expected_output1 = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NULL"],
        ["wrath", "anger", "NULL"]
    ]
    assert result1 == expected_output1, "Test case 1 failed!"

    print("All test cases passed!")
