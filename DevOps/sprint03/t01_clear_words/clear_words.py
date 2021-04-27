import re

def clear_words(s):
    return list(filter(None,list(map(str.strip, re.split(r" |\?|!|\.|:|;|,|-",s)))))
