import datetime

class ContaPoupanca:
   def __init__(self, taxaRemuneracao):
      self.taxaRemuneracao = taxaRemuneracao
      self.dataAbertura = datetime.datetime.today()
   
   def remuneracaoConta(self):
      self.saldo += (self.saldo * self.taxaRemuneracao)