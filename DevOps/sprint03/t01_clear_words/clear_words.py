import re

def re_sub_clean(string):
    return re.sub(r" |\?|!|\.|:|;|,|-","",string)

def clear_words(s):
    return list(map(re_sub_clean, s.split()))
