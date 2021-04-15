

def cube(int_num):
    while int_num != 0:
        yield(int_num**3)
        int_num -= 1
