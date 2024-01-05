n = 0
x = 0
y = 1
z = 1


while True:
    n = int(input("Ingresa un valor: "))
    if n > 0:
        break

""" print("1") """

""" for i in range(n-1):
    z = x + y
    print(f'{z}')
    x = y
    y = z """

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(n):
    print(f'{fibo(i+1)} ,')


