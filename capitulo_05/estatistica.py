#Estatística abrange conceitos matemáticos e técnicas para compreendermos os dados
from collections import Counter
import matplotlib.pyplot as plt
from typing import List

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def grafico_complexo_demais_para_apresentacao(num_friends):
    friends_counts = Counter(num_friends)
    xs = range(101) #o maior valor é 100
    ys = [friends_counts[x] for x in xs] #a altura indica o numero de amigos
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25]) #limites dos eixos x e y
    plt.title("Histograma de número de amigos")
    plt.xlabel("# de amigos")
    plt.ylabel("# de pessoas") 
    plt.show() 

def grafico_para_apresentacao(num_friends):
    num_points = len(num_friends)
    largest_value = max(num_friends) #100
    smallest_value = min(num_friends) #1
    
    sorted_values = sorted(num_friends)
    smallest_value = sorted_values[0] #1
    second_smallest_value = sorted_values[1] #1
    second_largest_value = sorted_values[-2] #49

#region TENDÊNCIAS CENTRAIS
'''valores que representam o centro ou a localização típica de um conjunto de dados.'''

#region MÉDIA
def mean(xs: List[float]) -> float:
    '''Retorna a média aritmética dos valores em xs.
    é influênciada pelo valor dos outliers(valores atípicos) e se o valor do índice 1 for aumentado, a média também aumenta.
    '''
    return sum(xs) / len(xs)
#endregion

#region MEDIANA

#mediana com elementos ímpares
def _median_odd(xs: List[float]) -> float:
    '''Retorna a mediana dos valores em xs quando xs tem um número ímpar(ODD) de elementos.
    é o valor do índice do meio quando os dados estão ordenados, não é influenciada por outliers, se valor de alguma posição mudar,
     o índice do meio continua sendo o mesmo.
    '''
    return sorted(xs)[len(xs) // 2]

# mediana com elementos pares
def _median_even(xs: List[float]) -> float:
    '''Retorna a mediana dos valores em xs quando xs tem um número par(EVEN) de elementos.
    mesma ideia da mediana ímpar, mas como não há um índice do meio, fazer a média dos dois valores centrais.
    '''
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2 #o índice do meio mais alto
    lo_midpoint = hi_midpoint - 1 #o índice do meio mais baixo
    return (sorted_xs[lo_midpoint] + sorted_xs[hi_midpoint]) / 2 #retorna a média dos dois valores centrais

#mediana geral
def median(v: List[float]) -> float:
    '''Retorna a mediana dos valores em v, seja v par ou ímpar.'''
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)
#assert median([1, 10, 2, 9, 5]) == 5
#assert median([1, 9, 2, 10]) == (2+9) / 2

#endregion

#region QUANTIL
'''quantis são valores que dividem um conjunto de dados ordenados em partes iguais.'''

def quantile(xs: List[float], p: float) -> float:
    '''Retorna o p-ésimo quantil dos valores em xs.
    separa uma determinada porcentagem dos dados ordenados.
    Por exemplo, o 0,5-ésimo quantil é a mediana(50%).
    '''
    p_index = int(p * len(xs)) #o índice do p-ésimo quantil
    return sorted(xs)[p_index]
#assert quantile(num_friends, 0.10) == 1
#assert quantile(num_friends, 0.25) == 3
#assert quantile(num_friends, 0.75) == 9
#assert quantile(num_friends, 0.90) == 13
#endregion

#region MODA
'''moda é o valor que aparece com mais frequência em um conjunto de dados.'''

def mode(x: List[float]) -> List[float]:
    '''Retorna uma lista pois pode haver mais de uma moda.'''
    counts = Counter(x) #um dicionário de valor -> contagem
    max_count = max(counts.values()) #a maior contagem
    return [x_i for x_i, count in counts.items() if count == max_count] #todos os valores com a maior contagem
#assert set(mode(num_friends)) == {1, 6}
#endregion

#endregion

#region DISPERSÃO
'''medidas que descrevem a variabilidade ou a dispersão dos dados.'''

#region AMPLITUDE
def data_range(xs: List[float]) -> float:
    '''Retorna a diferença entre o maior e o menor valor em xs.'''
    return max(xs) - min(xs)
#endregion

#endregion



#print(median(num_friends))