from ContaAgregada import ContaAgregada
from ContaPoupanca import ContaPoupanca
import datetime

class ContaRemuneradaPoupanca(ContaAgregada,ContaPoupanca):
   def __init__(self,taxaRemuneracao, clientes, numero, saldo, taxaCobranca):
      ContaAgregada.__init__(self,clientes, numero,saldo)
      ContaPoupanca.__init__(self,taxaRemuneracao)
      self.taxaCobranca = taxaCobranca

   def remuneraConta(self):
      self.saldo += self.saldo * (self.taxaRemuneracao/30)
      self.saldo -= self.taxaCobranca  