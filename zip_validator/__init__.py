import re

MIN_VALUE = 100000
MAX_VALUE = 999999


def in_range(number):
    p = re.compile('^[0-9]{6,6}$')
    return p.match(str(number))


def has_alternate_duplicates(number):
    digits = list(str(number))
    for i in range(4):
        if digits[i] == digits[i+2]:
            return False
    return True


def validate(val):
    if not in_range(val):
        return False

    number = int(val)

    if not MAX_VALUE > number > MIN_VALUE:
        return False

    if not has_alternate_duplicates(number):
        return False

    return True
