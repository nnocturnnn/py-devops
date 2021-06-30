import json
import math

def build_func(a, b, c):
    if a == 1:
        a = ""
    elif a == -1:
        a = "-"
    if b == 1:
        b = "+"
    elif b == -1:
        b = "-"
    elif b > 1:
        b = f"+{b}"
    if c >= 1:
        c = f"+{c}"
    elif c == 0:
        c = ""
    if b == 0:
        b = ""
        return f"{a}x^2{b}{c}=0"
    return f"{a}x^2{b}x{c}=0"

def math_func(a, b, c):
    my_formatter = "{0:.3f}"
    null = None
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return float(my_formatter.format(discr)), [float(my_formatter.format(x2)), float(my_formatter.format(x1))]
    elif discr == 0:
        x1 = -b / (2 * a)
        return float(my_formatter.format(discr)), float(my_formatter.format(x1))
    return float(my_formatter.format(discr)), null


def quad(a, b, c):
    if a == 0 or not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "Cannot generate a quadratic equation."
    dicty = {}.fromkeys(["equation","solution"])
    dicty["solution"] = {}.fromkeys(["discriminant","x"])
    dicty["equation"] = build_func(a,b,c)
    discr, x = math_func(a, b, c)
    dicty["solution"]["discriminant"] = discr
    dicty["solution"]["x"] = x
    return json.dumps(dicty, indent=3)

