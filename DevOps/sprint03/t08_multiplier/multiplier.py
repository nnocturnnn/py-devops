import functools


mult  = lambda x, y: x * y

def multiplier(arg_list):
    if not all(isinstance(x, (int, float)) for x in arg_list) \
        or not isinstance(arg_list, list) or len(arg_list) == 0:
        raise ValueError('The given data is invalid.')
    else:
        return functools.reduce(mult,arg_list)
