from quad import quad
from random import seed, randint


def run_test(a, b, c):
    print(f'---\n{a}, {b}, {c}')
    print(quad(a, b, c))


if __name__ == '__main__':
    run_test(1, 0, 0)
    run_test(-7.5, 0, 0)
    run_test(120, -1, 0)
    run_test(15, 1.8, 1)
    run_test(1, 4, 4)
    run_test(1, 5, 6)
    run_test('a', 5, 6)
    run_test(0, 1, 2)
    seed(5)
    for _ in range(3):
        run_test(randint(-20, 20), randint(-20, 20), randint(-20, 20))
