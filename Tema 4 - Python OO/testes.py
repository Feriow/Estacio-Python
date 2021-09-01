from Conta import Conta

conta1 = Conta(4444, '16846846', 'Amanda', 0)
conta2 = Conta(12345, '074.210.694-29', 'Valter', 0)

'''
print(conta.numero)
print(conta.cpf)
print(conta.nomeTitular)
print(conta.saldo)

print(conta2.numero)
print(conta2.cpf)
print(conta2.nomeTitular)
print(conta2.saldo)


conta.depositar(300)
conta.sacar(100)
conta.gerarExtrato()

# Os operadores “==” e “!=” comparam se as duas variáveis de referência apontam para 
# o mesmo endereço de memória

if conta1 != conta2: 
   print('Endereços diferentes de memória')

# O comando “=” realiza o trabalho de igualar a posição de duas referências na memória.
conta1 = conta2
if (conta1 == conta2):
   print("Enderecos iguais de memoria")
print(conta1.cpf)
print(conta2.cpf)

'''

conta1.depositar(1000)
conta1.transfereValor(conta2, 500)
conta1.gerarExtrato()
print('*************************')
conta2.gerarExtrato()
conta1.transfereValor(conta2, 10000)