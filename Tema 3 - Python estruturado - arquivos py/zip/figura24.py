def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)

regressiva(eval(input('Digite um número positivo: ')))