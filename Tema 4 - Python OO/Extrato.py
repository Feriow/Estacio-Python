class Extrato:
   def __init__(self):
      self.transacoes = []

   def imprimirExtrato(self, conta):
      print(f'Extrato : {conta.numero} \n')
      for p in self.transacoes:
         print(f' {p[0]:8s} {p[1]:10.2f} {p[2]} { p[3].strftime("%d/%m/%Y") } R${p[4]:8.2f}')