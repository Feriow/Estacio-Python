import datetime
from Extrato import Extrato

class ContaAgregada:
   def __init__(self, clientes, numero, saldo):
      self.clientes = clientes
      self.numero = numero
      self.saldo = saldo
      self.sataAbertura = datetime.datetime.today()
      self.extrato = Extrato()

   def depositar(self,valor):
      self.saldo += valor
      self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today(), self.saldo])
   
   def sacar(self,valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today(), self.saldo])
         return True

   def gerarExtrato(self):
      nomesClientes = ''
      for cliente in self.clientes:
         nomesClientes += cliente.nome + ' / '
      print(f" cliente(s): {nomesClientes } \n numero: {self.numero} \n saldo: {self.saldo}")

   def transfereValor(self, contaDestino, valor):
      if self.saldo < valor:
         print("Não existe saldo suficiente")
      else:
         contaDestino.depositar(valor)
         self.saldo -= valor
         self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
         print('Transferência realizada')