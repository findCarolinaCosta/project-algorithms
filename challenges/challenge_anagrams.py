def is_anagram(first_string, second_string):
    first = first_string.lower()
    second = second_string.lower()

    if (len(first) != len(second)):
        return False

    for character in first:
        if character not in second:
            return False

        if first.count(character) != second.count(character):
            return False

    return True
