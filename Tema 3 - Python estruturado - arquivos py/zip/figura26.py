def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n+1):
            fat = fat*x
        return fat

print(fatorial(eval(input('Digite um número positivo: '))))