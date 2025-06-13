def is_palindrome(s):
    return s == s[::-1]

# main
text = input("Enter a string: ")
print("Palindrome!" if is_palindrome(text) else "Not a palindrome.")
