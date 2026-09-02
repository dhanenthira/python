import re


def find_pattern(text, pattern):
    matches = re.findall(pattern, text)
    return matches
