#the result of the factorial of any number is that number multiply for the previous number until we reach 1
def factorial(n):
    if n == 0: #i don'tknow why but the factorial of 0 is 1
        return 1
    else:
        n>1
        return n*factorial(n-1)  #in case n is not 0 we multiply it for n-1 

resultado = factorial(5)
print(resultado) 