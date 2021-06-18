import json
import math

def build_func(a, b, c):
    if a == 1:
        a = ""
    elif b == 1:
        b = "+"
    elif a == -1:
        a = "-"
    elif b == -1:
        b = "-"
    elif b > 1:
        b = f"+{b}"
    if c >= 1:
        c = f"+{c}"
    return f"{a}x^2{b}x{c}=0"

def math_func(a, b, c):
    my_formatter = "{0:.2f}"
    null = None
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return discr, [my_formatter.format(x1), my_formatter.format(x2)]
    elif discr == 0:
        x1 = -b / (2 * a)
        return discr, my_formatter.format(x1)
    return discr, null


def quad(a, b, c):
    if a == 0 or not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "Cannot generate a quadratic equation."
    dicty = {}.fromkeys(["equation","solution"])
    dicty["solution"] = {}.fromkeys(["discriminant","x"])
    dicty["equation"] = build_func(a,b,c)
    discr, x = math_func(a, b, c)
    dicty["solution"]["discriminant"] = discr
    dicty["solution"]["x"] = x
    return json.dumps(dicty, indent=4)


def run_test(a, b, c):
    print(f'---\n{a}, {b}, {c}')
    print(quad(a, b, c))


run_test(1, 0, 0)
run_test(-7.5, 0, 0)
run_test(120, -1, 0)
run_test(15, 1.8, 1)
run_test(1, 4, 4)
run_test(1, 5, 6)
run_test('a', 5, 6)
run_test(0, 1, 2)