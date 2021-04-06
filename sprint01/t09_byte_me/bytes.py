


def convert_to_bytes(inty,booly,string):
    inty = int(inty)
    res_str = string.encode('utf-8')
    if booly == "True":
        res = 1
    else:
        res = 0
    res = bool(res)
    print(f'-- The int value is "{inty}"\n bytes: "{bytes(inty)}"')
    print(f'-- The string value is "{string}"\n bytes: "{res_str}"')
    print(f'-- The bool value is "{res}"\n bytes: "{bytes(res)}"')
