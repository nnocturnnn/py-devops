
def bubble_sort(arg_list):
    len_l = len(arg_list)
    for i in range(len_l - 1):
        for j in range(0, len_l - i - 1):
             if arg_list[j] > arg_list[j+1] :
                arg_list[j], arg_list[j+1] = arg_list[j+1], arg_list[j]