def taximetro(distancia=5, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


pagamento = taximetro(3,2)
pagamento2 = taximetro()
print(pagamento)
print(pagamento2)