import validators

email = input("What's your email address? ").strip()

if not validators.email(email):
    print("Invalid")
else:
    print("Valid")
