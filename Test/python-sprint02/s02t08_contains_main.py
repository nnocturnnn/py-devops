from contains import contains


if __name__ == '__main__':
    # define the test cases
    str1 = 'Ah, I see you have the machine that goes \'ping\'. '\
           'This is my favorite.'
    substr1 = ['ping', 'machine']

    str2 = 'Strange women lying in ponds, distributing swords, is no basis '\
           'for a system of government!'
    substr2 = ['strange', 'no, basis']

    # find the present words
    res1 = contains(str1, substr1)
    res2 = contains(str2, substr2)

    # print the result
    print('-----Agruments-----')
    print(f"'{str1}'\n{substr1}")
    print('-----Detected-----')
    print(res1)

    print('***')

    print('-----Agruments-----')
    print(f"'{str2}'\n{substr2}")
    print('-----Detected-----')
    print(res2)
