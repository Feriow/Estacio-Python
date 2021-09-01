# Treinamento supervisionado - classificação

from sklearn.tree import DecisionTreeClassifier

lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar = [[120,lisa],[140,lisa],[180,irregular],[200,irregular]]
resultado = [pera,pera,laranja,laranja]

#Gerar árvore de decisão
clf = DecisionTreeClassifier()

#Classificador
clf.fit(pomar, resultado)

#Variáveis de teste
frutas = [[220,irregular],[140,lisa],[150,lisa],[160,irregular]]

resultados = [clf.predict([fruta]) for fruta in frutas]

for resultado in resultados:
   if resultado == 1:
      print('Pera')
   else:
      print('Laranja')
