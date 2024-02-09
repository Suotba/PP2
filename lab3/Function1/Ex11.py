def is_palindrome(s):
    rev_s = ''.join(reversed(s))
    return s == rev_s

s = input("Enter a string: ")

print(is_palindrome(s))
