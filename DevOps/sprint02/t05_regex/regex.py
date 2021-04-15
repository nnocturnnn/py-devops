import re

def check_address(arg_dict):
    tpl = r'^Ukraine,[ ]*[A-Za-z-[ ]*]*,[ ]*[A-Za-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$'
    r_list = []
    for key in arg_dict:
        if re.match(tpl, arg_dict[key]) is not None:
            r_list.append(f"The address of {key} is valid.")
        else:
            r_list.append(f"The address of {key} is invalid.")
    return r_list
