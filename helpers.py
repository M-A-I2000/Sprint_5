import string
import random

def generate_email(domain="testsprint5.ru", length=8):
    characters = string.ascii_lowercase + string.digits
    local_part = ''.join(random.choice(characters) for _ in range(length))
    return f"{local_part}@{domain}"

def generate_password(length=12):
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    all_chars = lowercase + uppercase + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)