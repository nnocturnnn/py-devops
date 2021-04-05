

def list_maker(string, delim):
    if delim:
        return string.split(delim)
    else:
        return string.split()

