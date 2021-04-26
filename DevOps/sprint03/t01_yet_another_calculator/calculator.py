



def calculator(operator, f_num, s_num):
    try:
        div = {"add" : lambda x, y: x + y, "sub" : lambda x, y: x - y,
            "mul" : lambda x, y: x * y, "div" : lambda x, y: x / y,
            "pow" : lambda x, y: x ** y}
        lam = div[operator]
        try:
            print(lam(f_num,s_num))
        except:
            print("Invalid numbers. Second and third arguments must be numerical.")
    except:
        print("Invalid operation. Available operations: add, mul, div, pow, sub.")
