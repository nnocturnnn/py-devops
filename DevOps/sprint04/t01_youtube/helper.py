import sys


def print_stderr(arg):
    print("ERROR| " + arg,file=sys.stderr)

def print_stdout(arg):
    print("INFO| " + arg)