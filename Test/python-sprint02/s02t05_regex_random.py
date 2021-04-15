from regex import check_address
from random import randint, choice
from string import ascii_letters, digits, punctuation


def city_street(options=ascii_letters + ' -'):
    # random letters, spaces, hyphens (limit to 10 for readability)
    return ''.join((choice(options)) for _ in range(randint(1, 10)))


def get_number(n, options=digits):
    # random digits of given length
    return ''.join((choice(options)) for _ in range(n))


def comma():
    # comma + random spaces (up to 5 for readability)
    return ',' + ' ' * randint(0, 5)


def space():
    return ' ' * randint(1, 5)


def get_components():
    country = 'Ukraine'
    city = city_street()
    street_name = city_street()
    building = get_number(randint(1, 6))
    index = get_number(5)
    return country, city, street_name, building, index


def get_valid_address(components=get_components()):
    ukr, city, street, build, i = components
    return f'{ukr}{comma()}{city}{comma()}{street}{space()}{build}{comma()}{i}'


def invalid_cases():
    cases = []
    comp = list(get_components())
    comp[0] = 'ukraine'
    cases.append({'lowercase Ukraine': get_valid_address(comp)})
    comp = list(get_components())
    comp[0] = city_street()
    cases.append({'random str instead of Ukraine': get_valid_address(comp)})
    for _ in range(10):
        comp = list(get_components())
        comp[randint(1, 2)] += city_street('+=$%,' + digits)
        cases.append({'wrong chars': get_valid_address(comp)})
    for _ in range(10):
        comp = list(get_components())
        comp[randint(3, 4)] = \
            get_number(2) + get_number(3, ascii_letters + punctuation)
        cases.append({'wrong chars': get_valid_address(comp)})
    comp = list(get_components())
    comp[3] = get_number(7)
    cases.append({'wrong building': get_valid_address(comp)})
    comp = list(get_components())
    comp[4] = get_number(4)
    cases.append({'wrong index': get_valid_address(comp)})
    comp = list(get_components())
    comp[0] = 'bla ' + comp[0]
    cases.append({'rubbish before': get_valid_address(comp)})
    comp = list(get_components())
    comp[4] += 'bla'
    cases.append({'rubbish after': get_valid_address(comp)})
    return cases


def run_random_tests():
    # running tests with VALID addresses
    # if all correct, there will be no output
    for i in range(1000):
        test_dict = {'Name': get_valid_address()}
        result = check_address(test_dict)
        # uncomment the line below to see test cases printed
        # print(test_dict, result[0])
        if 'is invalid' in result[0]:
            print(f'Error. Test dict: {test_dict};'
                  f'Output: {result};Expected valid.')

    # running tests with INVALID addresses
    # if all correct, there will be no output
    for test_dict in invalid_cases():
        result = check_address(test_dict)
        # uncomment the line below to see test cases printed
        # print(test_dict, result[0])
        if 'is valid' in result[0]:
            print(f'Error. Test dict: {test_dict};'
                  f'Output: {result};Expected invalid.')
