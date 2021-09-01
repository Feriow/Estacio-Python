from ContaAgregada import ContaAgregada
import datetime

# HERANÇA - A classe pai vai dentro dos parênteses da classe filha. Usar super() para inicializar
# a parte da classe pai. Para reescrever metódos, usar o mesmo nome.

class ContaEspecial(ContaAgregada):
   def __init__(self, clientes, numero, saldo, limite):
      super().__init__(clientes, numero, saldo)
      self.limite = limite
   
   def sacar(self,valor):
      if (self.saldo + self.limite) < valor:
         return False
      else:
         self.saldo -= valor
         self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today(), self.saldo])
         return True