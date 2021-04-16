

def fib(nterms):
    n1, n2 = 0, 1
    count = 0

    if nterms == 1:
        return n1
    else:
        while count < nterms:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return n1


def fib_generator(nterms):
    n1, n2 = 0, 1
    count = 0

    if nterms == 1:
        yield n1
    else:
        while count < nterms:
            yield n1
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

