


def print_str_analytics(string):
    isspace = isupper = islower = isdecim = isalpha = isalphanum = isprint = 0
    for i in string:
        isalpha += 1 if i.isalpha() else 0
        isprint += 1 if i.isprintable() else 0
        isalphanum += 1 if i.isalnum() else 0
        isdecim += 1 if i.isdecimal() else 0
        islower += 1 if i.islower() else 0
        isupper += 1 if i.isupper() else 0
        isspace += 1 if i.isspace() else 0
    print(f"""|------------------------------------------------|
|                String analytics                |
|------------------------------------------------|
| '{string}'                       
|------------------------------------------------|
| Number of printable characters is: {isprint}
| Number of alphanumeric characters is: {isalphanum}
| Number of alphabetic characters is: {isalpha}
| Number of decimal characters is: {isdecim}
| Number of lowercase letters is: {islower}
| Number of uppercase letters is: {isupper}
| Number of whitespace characters is: {isspace}
|------------------------------------------------|
             """)

print_str_analytics("We are three wise men!")