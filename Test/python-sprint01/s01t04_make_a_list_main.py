# s01t04_make_a_list_main.py
from list_maker import list_maker


if __name__ == '__main__':
    line, delim = 'surprise', '-'
    res = list_maker(line, delim)
    print(f'Our chief weapon is {res}'
          f'... surprise and fear... fear and surprise...')
    # joining the result back into a string using the delimiter
    # must create a string identical to the original one
    if delim.join(res) != line:
        print('Error.')

    line, delim = 'fear;surprise', ';'
    res = list_maker(line, delim)
    print(f'Our {len(res)} weapons are {res} and ruthless efficiency.')
    if delim.join(res) != line:
        print('Error.')

    line, delim = 'fearblasurpriseblaruthless efficiency', 'bla'
    res = list_maker(line, delim)
    print(f'Our {len(res)} weapons are {res},\n\tand '
          f'an almost fanatical devotion to the Pope.')
    if delim.join(res) != line:
        print('Error.')

    line += 'blaan almost fanatical devotion to the Pope'
    res = list_maker(line, delim)
    print(f'Our {len(res)}, no... Amongst our weaponry are such elements as:\n'
          f'\t{res},\n\tand nice red uniforms - Oh damn!\n')
    if delim.join(res) != line:
        print('Error.')

    line, delim = 'abracadabra', 'b'
    res = list_maker(line, delim)
    print(f'Original string: `{line}`; delimiter: `{delim}`;\n\tresult: {res}')
    if delim.join(res) != line:
        print('Error.')

    line, delim = '', '*'
    res = list_maker(line, delim)
    print(f'Original string: `{line}`; delimiter: `{delim}`;\n\tresult: {res}')
    if delim.join(res) != line:
        print('Error.')

    line, delim = 'testing.extra.delims.in.the.end..', '.'
    res = list_maker(line, delim)
    print(f'Original string: `{line}`; delimiter: `{delim}`;\n\tresult: {res}')
    if delim.join(res) != line:
        print('Error.')
