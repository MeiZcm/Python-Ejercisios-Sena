def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

num1 = 69
num2 = 24

resultado = mcd(num1, num2)

print(resultado)
