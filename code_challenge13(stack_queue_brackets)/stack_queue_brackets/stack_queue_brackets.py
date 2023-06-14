def validate_brackets(string):
    """
    Validate if the brackets in the string are balanced.

    Args:
        string (str): The input string to check for balanced brackets.

    Returns:
        bool: True if the brackets are balanced, False otherwise.

    """
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                print(f"Error: Closing bracket {char} arrived without corresponding opening.")
                return False
            opening_bracket = stack.pop()
            closing_bracket = bracket_pairs[opening_bracket]
            if char != closing_bracket:
                print(f"Error: Closing bracket {char} doesn't match opening bracket {opening_bracket}.")
                return False

    if stack:
        opening_bracket = stack.pop()
        print(f"Error: Unmatched opening bracket {opening_bracket} remaining.")
        return False

    return True
