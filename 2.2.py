def check_strength(password):
    big = False
    small = False
    number = False
    symbol = False

    for ch in password:
        if ch.isupper():
            big = True
        elif ch.islower():
            small = True
        elif ch.isdigit():
            number = True
        else:
            symbol = True

    if len(password) >= 8 and big and small and number and symbol:
        return "Strong"
    elif len(password) >= 6:
        return "Moderate"
    else:
        return "Weak"

#main
word = input("Enter password: ")
print("Password is", check_strength(word))
