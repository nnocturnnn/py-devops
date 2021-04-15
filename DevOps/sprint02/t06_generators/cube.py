

def cube(int_num):
    if int_num > 0:
        while int_num != 0:
            yield(int_num**3)
            int_num -= 1
