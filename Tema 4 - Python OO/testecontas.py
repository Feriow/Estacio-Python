from ContaAgregada import ContaAgregada
from ContaEspecial import ContaEspecial
from ContaPoupanca import ContaPoupanca
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca
from Cliente import Cliente

cliente1 = Cliente(123, 'Joao', 'Rua 1')
cliente2 = Cliente(345, 'Maria', 'Rua 2')
cliente3 = Cliente (789,"Joana", "Rua H")
conta1 = ContaAgregada([cliente1, cliente2], 1, 2000)
conta2 = ContaEspecial([cliente3], 3, 1000,2000)
contaPoupanca1 = ContaPoupanca(0.1)
contarenumerada1 = ContaRemuneradaPoupanca(0.1,[cliente1],5,1000,5)
contarenumerada1.remuneraConta()
contarenumerada1.gerarExtrato()

#conta2.depositar(100)
#conta2.sacar(3000)
#conta2.extrato.imprimirExtrato(conta2)

'''
#conta1.gerarExtrato()
conta1.extrato.imprimirExtrato(conta1)
conta1.depositar(1500)
conta1.sacar(500)
conta1.sacar(200)
#conta1.gerarExtrato()
conta1.extrato.imprimirExtrato(conta1)

#print(f'\n Cliente: {cliente1.nome} / Endereço: {cliente1.endereco}')
#print(f'\n Cliente: {cliente2.nome} / Endereço: {cliente2.endereco}')

'''
