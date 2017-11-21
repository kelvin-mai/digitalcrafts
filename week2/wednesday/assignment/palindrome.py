def is_palindrome(word):
    return word[::-1].lower().replace(' ','') == word.lower().replace(' ','')
