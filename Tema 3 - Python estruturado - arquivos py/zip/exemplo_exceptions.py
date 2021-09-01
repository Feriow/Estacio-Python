
try:
   numerador = eval(input('Entre com o numerador da fração: '))
   denominador = eval(input('Entre com o denominador da fração: '))
   print(f'A divisão vale {numerador/denominador}')
except ZeroDivisionError:
   print('O denominador não pode ser 0')
except:
   print('Os parâmetros informados são inválidos')
finally:
   print('*** Programa encerrado ***')

'''
   Exceção	                  Explicação
KeyboardInterrupt    Levantado quando o usuário pressiona CTRL + C, a combinação de interrupção.
OverflowError	      Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
ZeroDivisionError	   Levantado quando se tenta dividir por 0.
IOError	            Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
IndexError	         Levantado quando um índice sequencial está fora do intervalo de índices válidos.
NameError	         Levantado quando se tenta avaliar um identificador (nome) não atribuído.
TypeError	         Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
ValueError	         Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.
'''