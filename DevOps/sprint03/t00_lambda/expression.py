
n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

result = lambda a, b, n : n % a == 0 and n % b == 0

print(result(a,b,n))