"""Module that provides is_palindrome.

Author of is_palindrome: Ambika
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the last character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns if word is a is palindrome or not.

    word: string

    returns: boolean
    """
    if len(word)<=1:
        return True
    if first(word)!=last(word):
        return False
    return is_palindrome(middle(word))

print is_palindrome('noon')
print is_palindrome('cars')
