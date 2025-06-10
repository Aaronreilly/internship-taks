def is_valid_email(email):
    if "@" in email and "." in email:
        at = email.index("@")
        dot = email.rindex(".")

        if at < dot and at > 0 and dot < len(email) - 1:
            return True
    return False

# main
user_email = input("Enter your email: ")

if is_valid_email(user_email):
    print("Valid email.")
else:
    print("Invalid email.")
