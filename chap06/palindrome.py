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

    word:string

    returns: length 1 string
    """
    return word[-1]
def middle(word):
    """Returns all but the first and last character of a word.

    word:string

    returns:string
    """
    return word[1:-1]

def is_palindrome(word):
    """Returns is word is a palindrome or not.

    word: string of more than 2 characters

    returns: boolean
    """
    if first(word)==last(word):
        if len(word)<4:
            return True
        else:
            return is_palindrome(middle(word))
    else:
        return False


print is_palindrome('redivider')
print is_palindrome('noon')
print is_palindrome('cars')
print is_palindrome('bab')
