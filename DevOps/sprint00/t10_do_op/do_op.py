print("---- Simple calculator ----\nLet's add some numbers")
f_num = int(input("Input your first value: "))
operand = input("Input your operator: ")
s_num = int(input("Input your second value: "))
if operand == "+":
    print(f"{f_num} + {s_num} = {f_num + s_num}")
elif operand == "-":
    print(f"{f_num} - {s_num} = {f_num - s_num}")
elif operand == "*":
    print(f"{f_num} * {s_num} = {f_num * s_num}")
elif operand == "/":
    print(f"{f_num} / {s_num} = {f_num / s_num}")
else:
    print("usage: the operator must be'*' or '+' or '-' or '/'")
print("---- Simple calculator ----")