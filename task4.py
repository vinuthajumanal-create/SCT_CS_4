import re

def evaluate_password(password):
    score = 0
    feedback = []


    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length (minimum 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        feedback.append("Avoid common passwords")
        score = 0

    if score >= 6:
        strength = "Very Strong 💪"
    elif score >= 4:
        strength = "Strong 👍"
    elif score >= 3:
        strength = "Medium ⚖️"
    else:
        strength = "Weak ⚠️"

    return strength, feedback

print("=== Advanced Password Strength Checker ===")
password = input("Enter your password: ")

strength, feedback = evaluate_password(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for f in feedback:
        print("-", f)
else:
    print("\nExcellent password! No improvements needed.")
