from regex import check_address
from s02t05_regex_random import run_random_tests


dictionary = {
        'Dmitry Chaykin': '   Ukraine ,  Kyiv  ,  Dorohozhytska    3,  04119 ',
        'Andrey Myskin': 'Ukraine, Lviv, Volodymyra Velykoho 52, 79053',
        'Tatyana Tsareva': 'Ukraine, Kyiv , Mykola Grinchenko 4, 03038',
        'Zhanna Akopyan': 'Ukraine, Kharkiv, 23 August 33, 61000',
        'Viktor Vasilyev': 'Ukraine, 5 Pasternaka Street Lviv 79000',
        'Andrey Sharov': '271 Akademika Pavlova Street, Kharkiv, Ukraine',
    }


if __name__ == '__main__':
    print(*check_address(dictionary), sep='\n')
    run_random_tests()
