import secrets
import string

password_question = int(
    input('How many characters do you want to generate?": '))
complexity_question = int(
    input('what is the level of complexity of the characters?": '))
safe_password = ''


def complexity(q):
    return secrets.choice(str(secrets.token_bytes(q)) + string.ascii_letters + str(
        secrets.token_urlsafe(q)) + string.digits + str(secrets.token_hex(q)) + string.punctuation)


for i in range(password_question):
    safe_password += complexity(complexity_question)

print(f"Your safe password is: {safe_password}")
