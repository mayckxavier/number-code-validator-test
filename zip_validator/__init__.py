import re


def validate(number):
    p = re.compile('^[0-9]{6,6}$')
    if not p.match(str(number)):
        return False

    if number <= 100000:
        return False
    elif number >= 999999:
        return False

    return True
