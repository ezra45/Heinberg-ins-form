import phonenumbers
from email_validator import validate_email, EmailNotValidError

def is_valid_name(name, allow_empty=False):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'- ,.`~")
    if allow_empty and name == "":
        return True
    if len(name) < 2 or len(name) > 100:
        return False
    return all(char in allowed for char in name)

def is_valid_address(address):
    return 3 <= len(address) <= 200

def is_valid_phone(phone):
    try:
        return phonenumbers.is_valid_number(phonenumbers.parse(phone, "US"))
    except phonenumbers.NumberParseException:
        return False

def is_valid_email(email):
    try:
        valid = validate_email(email)
        email = valid.email
        return True
    except EmailNotValidError:
        return False