



def calculator(operator, f_num, s_num):
        div = {"add" : lambda x, y: x + y, "sub" : lambda x, y: x - y,
            "mul" : lambda x, y: x * y, "div" : lambda x, y: x / y,
            "pow" : lambda x, y: x ** y}
        if operator not in div:
            raise ValueError("Invalid operation. Available operations: add, mul, div, pow, sub.")
        lam = div[operator]
        if (type(f_num) != int and type(f_num) != float and type(f_num) != complex) or \
            (type(s_num) != int and type(s_num) != float and type(s_num) != complex): 
            raise ValueError("Invalid numbers. Second and third arguments must be numerical")
        print(lam(f_num,s_num))
            
