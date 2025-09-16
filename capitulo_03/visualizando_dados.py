#Visualização de dados é a arte de comunicar informações através de representações gráficas

import matplotlib.pyplot as plt
from collections import Counter

def grafico_barras():
    '''Gráfico de barras pg.48
    boa opção para mostrar variação de quantidade em um conjunto discreto de itens
    '''
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

def grafico_linhas():
    '''
    Gráfico de linhas pg.50
    útil para mostrar tendências ao longo do tempo (séries temporais)
    '''
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    #podemos fazer varias chamadas para plt.plot para mostrar múltiplas séries no mesmo gráfico
    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')

    #como atribuimos rotulos a cada serie, podemos criar uma legenda de graça (loc=9 é igual a "top center")
    plt.legend(loc=9)
    plt.xlabel("complexidade do modelo")
    plt.xticks([])
    plt.title("Acurácia do Modelo")
    plt.show()

def grafico_dispersao():
    '''
    Gráfico de dispersão pg.49
    útil para mostrar a relação entre dois conjuntos de dados
    representar as relações entre pares de conjunto de dados ex: relação entre amigos dos usuários e os minutos que eles passam no site por dia
    '''
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    #nomeia cada ponto
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                    xy=(friend_count, minute_count), # Coloque o rótulo no respectivo ponto
                    xytext=(5, -5), #mas levemente deslocado
                    textcoords='offset points')

    plt.title("Minutos Diários vs. Número de Amigos")
    plt.xlabel("# de amigos")
    plt.ylabel("minutos diários passados no site")
    plt.show()

grafico_dispersao()