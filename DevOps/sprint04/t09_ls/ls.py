import os
import sys


def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)  
    second_ele = list.pop(pos2-1)
    list.insert(pos1, second_ele) 
    list.insert(pos2, first_ele) 
     
    return list

def fun_ls():
    # all_flag = ["-l","-R","-lR","-Rl"]
    argvs = sys.argv
    if len(argvs) > 2:
        argvs = swapPositions(argvs, 1, 2)
    argvs[0] = "ls"
    argc = " ".join(argvs)
    os.system(argc)




fun_ls()