def is_palindrome_number(num):
    num_str = str(num)

    reversed_str = num_str[::-1]
    if num_str == reversed_str:
        return True
    else:
        return False

# Test the function
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
