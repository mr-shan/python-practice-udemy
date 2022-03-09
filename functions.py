def multiply(x: float, y: float = 1) -> float:
    """
    Multiply two numbers.

    :param x: The first number to multiply
    :param y: The second number to multiply with `x`
    :return: The product of `x` and `y`. Returns either `int` or `float`
    """
    return x * y


def is_palindrome(string: str = "") -> bool:
    """
    Check if the string passed is palindrome.

    :param string: String to check
    :return: True or False based on palindrome
    """
    string = string.casefold().replace(" ", "")

    filtered_string = ""
    for char in string:
        if char.isalnum():
            filtered_string += char

    string_length = len(filtered_string)
    for i in range(0, string_length // 2):
        if filtered_string[i] == filtered_string[string_length - 1 - i]:
            continue
        else:
            return False
    return True

