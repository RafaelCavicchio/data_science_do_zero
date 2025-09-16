'''
Gráfico de barras pg.48
boa opção para mostrar variação de quantidade em um conjunto discreto de itens
'''

from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

#Agrupe as notas por decil, mas coloque o 100 com o 90
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

print(histogram.keys())
plt.bar([x + 5 for x in histogram.keys()], #move as barras para a direita em 5
        histogram.values(), #Atribua a altura correta a cada barra
        10, #largura 10 a cada barra
        edgecolor=(0, 0, 0)) #Escurece as bordas das barras

plt.axis([-5, 105, 0, 5]) #eixo x de -5 a 105 e eixo y de 0 a 5

plt.xticks([10 * i for i in range(11)]) #rótulos do eixo x em 0,10 ...., 100
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas do Teste 1")
plt.show()