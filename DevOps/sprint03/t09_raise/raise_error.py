


def raise_error(key: str, mess: str):
    if key == 'value':
        raise ValueError(mess)
    elif key == 'key':
        raise KeyError(mess)
    elif key == 'index':
        raise IndexError(mess)
    elif key == 'memory':
        raise MemoryError(mess)
    elif key == 'name':
        raise NameError(mess)
    elif key == 'eof':
        raise EOFError(mess)
    raise ValueError('No error with such key.')
