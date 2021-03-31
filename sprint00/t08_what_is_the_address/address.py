


first_var = 1000
second_var = 1000
third_var = 999
print(f"first_var = {first_var}, address is {id(first_var)}\n \
second_var = {second_var}, address is {id(second_var)}\n \
third_var = {third_var}, address is {id(third_var)}\n \
{first_var} is {second_var} = {bool(first_var is second_var)}\n \
{first_var} is {third_var} = {bool(first_var is third_var)}")