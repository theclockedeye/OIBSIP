# utils/password_generator.py
import random
import string
import pyperclip  # For clipboard functionality

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    char_sets = []

    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("At least one character set must be selected.")

    all_characters = ''.join(char_sets)
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)
