from clear_words import clear_words


text_example_1 = 'WOMAN: Yes?, ENCYCLOPEDIA SALESMAN: Burglar, madam. WOMAN: '\
                 'Are you an encyclopaedia salesman?'

text_example_2 = 'ENCYCLOPEDIA SALESMAN: No madam, I\'m a burglar, '\
                 'I burgle people. WOMAN: I think you\'re an encyclopaedia '\
                 'salesman.'

text_example_3 = 'ENCYCLOPEDIA SALESMAN: Oh I\'m not, open the door, '\
                 'let me in please. WOMAN: If I let you in, you\'ll sell '\
                 'me encyclopedias.'


if __name__ == '__main__':
    result = clear_words(text_example_1)
    print(result)

    result = clear_words(text_example_2)
    print(result)

    result = clear_words(text_example_3)
    print(result)
