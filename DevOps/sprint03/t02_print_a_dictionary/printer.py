


def dictionary_printer(arg_dict):
    if not isinstance(arg_dict, dict):
        raise ValueError("The argument must be a dict.")
    return list(map(lambda d : str(d[0]) + ' - ' + str(d[1]) ,arg_dict.items()))

