import os

from read_file import read_file

if __name__ == '__main__':
    strings = ['sample.txt', 'sample1.txt', 'no_permission.txt']
    # remove read permissions from one file to check error handling
    os.chmod('no_permission.txt', 000)
    for string in strings:
        read_file(string)
        print('***')
