python

```python

import re
import getpass
import string

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters for better security.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password):
        score += 1
    else:
        feedback.append("Add at least one special symbol.")

    if not re.search(r"(.)\1\1", password):
        score += 1
    else:
        feedback.append("Avoid repeating the same character three times.")

    common_passwords = [
        "password", "12345678", "qwerty123",
        "admin123", "welcome123", "password123"
    ]

    if password.lower() not in common_passwords:
        score += 1
    else:
        feedback.append("Avoid commonly used passwords.")

    if not re.search(r"(123|abc|qwerty|password)", password.lower()):
        score += 1
    else:
        feedback.append("Avoid predictable sequences and words.")

    if score <= 3:
        strength = "WEAK"
        symbol = "🔴"
    elif score <= 6:
        strength = "MEDIUM"
        symbol = "🟡"
    else:
        strength = "STRONG"
        symbol = "🟢"

    print("\n PASSWORD REPORT ")
    print("Password Length:", len(password))
    print("Security Score:", score, "/ 9")
    print("Password Strength:", symbol, strength)

    if feedback:
        print("\nSuggestions to Improve:")
        for item in feedback:
            print("-", item)
    else:
        print("\nExcellent! Your password meets all checks.")

def main():
    print("PASSWORD STRENGTH CHECKER")
    while True:
        password = getpass.getpass("\nEnter your password: ")

        if not password:
            print("Password cannot be empty!")
            continue

        check_password(password)

        choice = input("\nCheck another password? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for using Password Strength Checker!")
            break


if password-checker.py == "__main__":
    main()
```
