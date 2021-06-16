import sys


def print_stderr(arg):
    print(arg,file=sys.stderr)

def print_stdout(arg):
    print("INFO| " + arg)