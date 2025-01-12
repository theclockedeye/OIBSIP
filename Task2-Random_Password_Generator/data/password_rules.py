# data/password_rules.py

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 16

def validate_length(length):
    if length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password length should be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}.")
    return True
