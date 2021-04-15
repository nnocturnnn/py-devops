from unique import make_unique


test_case_1 = {
  "city": ['Kharkiv', 'Kyiv', 'Lviv', 'Dnipro', 'Kyiv', 'Kyiv', 'Kharkiv',
           'Kharkiv', 'Lviv'],
  "age": [16, 16, 17, 18, 19, 19, 19, 18, 20],
}
test_case_2 = {
  "hobby": ['drawing', 'basketball', 'drawing', 'drawing', 'basketball',
            'dancing', 'dancing', 'dancing', 'dancing'],
  "format": ['individually', 'individually', 'group', 'individually', 'group',
             'individually', 'group', 'group', 'group'],
}


if __name__ == '__main__':
    print('-----Before-----')
    print(test_case_1)
    print('-----After-----')
    print(make_unique(test_case_1))

    print('***')
    print('-----Before-----')
    print(test_case_2)
    print('-----After-----')
    print(make_unique(test_case_2))
