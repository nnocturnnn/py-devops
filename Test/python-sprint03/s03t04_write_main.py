from write_file import write_file

if __name__ == '__main__':

    write_file('file')
    print('***')
    write_file('file.txt')
    print('***')
    write_file('file', 'Hello there')
    print('***')
    write_file('new_file.txt', 'Hello there')
    print('***')
    # check with a non-empty file
    write_file('example.txt', 'A new message')
    print('***')
