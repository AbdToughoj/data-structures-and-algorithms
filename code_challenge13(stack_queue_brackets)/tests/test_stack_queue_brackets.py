from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_validate_brackets_one():
    input_string = "{}"
    expected_output = True

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_two():
    input_string = "{}(){}"
    expected_output = True

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_three():
    input_string = "()[[Extra Characters]]"
    expected_output = True

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_four():
    input_string = "(){}[[]]"
    expected_output = True

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_five():
    input_string = "{}{Code}[Fellows](())"
    expected_output = True

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_six():
    input_string = "[({}]"
    expected_output = False

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_seven():
    input_string = "]("
    expected_output = False

    result = validate_brackets(input_string)
    assert result == expected_output

def test_validate_brackets_eight():
    input_string = "{(})"
    expected_output = False

    result = validate_brackets(input_string)
    assert result == expected_output

