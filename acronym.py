import string
import re
def abbreviate(words):
    ## split the phrase into substrings
    words_split = words.split()
    
    """Turn a list of words into an acronym"""
    #replace punctuation with white space if word not in string.punctuation else ''
    return "".join(word[0] if word not in string.punctuation else '' for word in words_split).upper()
    
    #return re.sub(r'\W*(\w)\w*\W*', r'\1', words.upper())