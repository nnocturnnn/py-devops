
import re

def clear_words(arg_str):
    string = re.split('? |! |. |: |; |, |-', arg_str)
    print(string)
    # l = list(map(lambda x: x, re.split('? |! |. |: |; |, |-', arg_str)))
    # print(l)


text_example_1 = 'WOMAN: Yes?, ENCYCLOPEDIA SALESMAN: Burglar, madam. WOMAN: '\
                 'Are you an encyclopaedia salesman?'

clear_words(text_example_1)