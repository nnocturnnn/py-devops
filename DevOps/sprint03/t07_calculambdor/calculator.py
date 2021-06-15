

operations = {"add" : lambda x, y: x + y, "sub" : lambda x, y: x - y,
              "mul" : lambda x, y: x * y, "div" : lambda x, y: x / y,
              "pow" : lambda x, y: x ** y}


def calculator(operator, f_num, s_num):
        if operator not in operations:
            raise ValueError("Invalid operation. Available operations: add, mul, div, pow, sub.")
        lam = operations[operator]
        if (type(f_num) != int and type(f_num) != float and type(f_num) != complex) or \
            (type(s_num) != int and type(s_num) != float and type(s_num) != complex): 
            raise ValueError("Invalid numbers. Second and third arguments must be numerical")
        return lam(f_num,s_num)