import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas

#############      Pré-processamento     ###############
# Coleta e Integração
arquivo = pandas.read_csv('dados_dengue.csv')

anos = arquivo[['ano']]
casos = arquivo[['casos']]

##############       Mineração        #################
regr = LinearRegression()
regr.fit(X=anos, y=casos)

ano_futuro1 = [[2018]]
ano_futuro2 = [[2019]]
casos_2018 = regr.predict(ano_futuro1)
casos_2019 = regr.predict(ano_futuro2)

print('Casos previstos para 2018 ->', int(casos_2018))
print('Casos previstos para 2019 ->', int(casos_2019))

############      Pós-processamento     ################
plt.scatter(anos, casos, color='black')
plt.scatter(ano_futuro1, casos_2018, color='red')
plt.scatter(ano_futuro2, casos_2019, color='orange')
plt.plot(anos, regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([[2018],[2019]])
plt.yticks([[int(casos_2018)],[int(casos_2019)]])

plt.show()