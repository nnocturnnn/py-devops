

def validator(arg):
    arg_list = arg.split()
    try:
        arg_list[0] = float(arg_list[0])
        arg_list[2] = float(arg_list[2])
    except:
        return False
    if arg_list[1] == ">":
        arg_list[1] = True if arg_list[0] > arg_list[2] else "<"
    elif arg_list[1] == "<":
        arg_list[1] = True if arg_list[0] < arg_list[2] else ">"
    elif arg_list[1] == ">=":
        arg_list[1] = True if arg_list[0] >= arg_list[2] else "<="
    elif arg_list[1] == "<=":
        arg_list[1] = True if arg_list[0] <= arg_list[2] else ">="
    elif arg_list[1] == "==":
        if arg_list[0] == arg_list[2]:
            arg_list[1] = True
        elif arg_list[0] < arg_list[2]: 
            arg_list[1] = "<="
        else:
            arg_list[1] = ">="
    else:
        return False
    if arg_list[1] == True:
        return True
    else:
        return str(arg_list[0]) + " " + arg_list[1] + " " + str(arg_list[2])
    
