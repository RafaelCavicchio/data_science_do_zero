#Estatística abrange conceitos matemáticos e técnicas para compreendermos os dados
from collections import Counter
import matplotlib.pyplot as plt
from typing import List
import math
import sys
import os
sys.path.append(os.getcwd())
from capitulo_04.algebra_linear import sum_of_squares, dot

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,
               11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,
               9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,
               6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,
               4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
               3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,
                 47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,
                 39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,
                 24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,
                 36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,
                 29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,
                 35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,
                 39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,
                 14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,
                 26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,
                 25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,
                 36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,
                 25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,
                 35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,
                 13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,
                 21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

daily_hours = [dm / 60 for dm in daily_minutes]


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
    '''Média \n
    Retorna a média aritmética dos valores em xs.
    é influênciada pelo valor dos outliers(valores atípicos) e se o valor do índice 1 for aumentado, a média também aumenta.
    '''
    return sum(xs) / len(xs)
#endregion

#region MEDIANA

#mediana com elementos ímpares
def _median_odd(xs: List[float]) -> float:
    '''MEDIANA Retorna a mediana dos valores em xs quando xs tem um número ímpar(ODD) de elementos.
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
    '''MEDIANA -> Retorna a mediana dos valores em v, seja v par ou ímpar.
    verifica se o número de elementos do array é par ou impar e chama a função correta para calcular a mediana.
    Args:
        v (List[float]): Array contendo os dados
    Returns:
        float: Valor do índice que se encontra no meio do array (50% do array)
    '''
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)
#assert median([1, 10, 2, 9, 5]) == 5
#assert median([1, 9, 2, 10]) == (2+9) / 2

#endregion

#region QUANTIL
'''quantis são valores que dividem um conjunto de dados ordenados em partes iguais.'''

def quantile(xs: List[float], p: float) -> float:
    '''QUANTIL -> separa uma determinada porcentagem dos dados ordenados.
    Por exemplo, o 0.5-ésimo quantil é a mediana(50%).

    Args:
        xs (List[float]): Array contendo os dados.
        p (float): porcentagem dos dados que queremos, ex: 0.25
    Returns:
        float: Valor que representa o p-ésimo quantil de xs.    
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
    '''Moda \n
    Retorna uma lista pois pode haver mais de uma moda.'''
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
    '''AMPLITUDE
    Args:
        xs (List[float]): Array contendo os dados.
    Returns:
        float: Retorna a diferença entre o maior e o menor valor em xs
    '''
    return max(xs) - min(xs)
#endregion

#region DESVIO
def de_mean(xs: List[float]) -> List[float]:
    '''DESVIO -> calculamos a média do array e subtraímos os valores do array com a média, assim temos o desvio.
    Args:
        xs (List[Float]): Array com os dados.
    Returns:
        List[Float]: Nova array contendo o desvio
    '''
    x_bar = mean(xs)
    return [x - x_bar for x in xs]
#endregion

#region VARIÂNCIA
def variance(xs: List[float]) -> float:
    '''VARIÂNCIA -> é a média dos quadrados dos desvios. \n
    A variância mede quanto os dados se espalham em relação à média \n
    Formula:
        VAR(X) = (1/(n-1)) * Σ(xi - x̄)²
    xi: valores da amostra
    x̄: média da amostra
    n: número de elementos na amostra
    1/(n-1): graus de liberdade, usado para corrigir o viés na estimativa da variância populacional a partir de uma amostra.
    ²: calcumamos o quadrado dos desvios para eliminar dados negativos e dar mais peso aos desvios maiores.
        
    Args:
        xs (List[float]): Array contendo os dados.
    Returns:
        float: Retorna a variância dos valores do array.
    '''
    assert len(xs) >=2, "A variancia requer ao menos 2 elementos no array"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1) #dividimos por n-1 e não n para corrigir o viés na estimativa da variância populacional
#assert 81.54 < variance(num_friends) < 81.55
#endregion

#region DESVIO PADRÃO
def standard_deviation(xs : List[float]) -> float:
    '''DESVIO PADRÃO -> É a raiz quadrada da Variância! mede a dispersão ou a variação de um conjunto de dados em relação à sua média'''
    return math.sqrt(variance(xs))
#assert 9.02 < standard_deviation(num_friends) < 9.04
#endregion

#region INTERVALO INTERQUARTIL
def interquartile_range(xs: List[float]) -> float:
    """INTERVALO INTERQUARTIL -> retorna a diferença entre quantis, ex 75% - 25% dos dados. ajuda a reduzir o impacto dos outliers
    Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)
#assert interquartile_range(num_friends) == 6
#endregion

#region COVARIÂNCIA
def covariance(xs: List[float], ys: List[float]) -> float:
    '''COVARIÂNCIA -> Fazemos o mesmo que na variância, mas agora multiplicando os desvios de xs e ys ao invés de elevarmos xs ao quadrado.
    serve para medir como duas variáveis variam juntas. \n
    covariância responde a seguinte pergunta: quando xs aumenta, ys também aumenta (positivo) ou diminui (negativo)? \n
    Formula: \n
    Cov(X,Y) = Σ[(xi - x̄)(yi - ȳ)] / (N-1) \n
    Σ (Sigma): O símbolo do somatório, que indica que devemos somar todos os produtos dos desvios. \n
    xi: O i-ésimo valor da variável X no conjunto de dados. \n
    x̄ (x barra): A média de todos os valores da variável X. \n
    yi: O i-ésimo valor da variável Y no conjunto de dados. \n
    ȳ (y barra): A média de todos os valores da variável Y. \n
    n: O número total de itens (pares de dados) no conjunto de dados. \n
    (n - 1): Na fórmula da covariância amostral, divide-se por n - 1 para obter um estimador não enviesado da covariância populacional. \n
    Args:
        xs (List[float]): Array x
        ys (List[float]): Array y
    Returns:
        float: retorna o valor da covariância entre xs e ys
    '''
    assert len(xs) == len(ys), "xs e ys deve ter o mesmo número de elementos"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1) #o dot soma os produtos dos pares de elementos correspondentes.

#assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
#assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60
#endregion

#region CORRELAÇÃO

def correlation(xs: List[float], ys: List[float]) -> float:
    '''CORRELAÇÃO -> é a covariância dividida pelo produto do desvio padrão de xs e o desvio padrão de ys. \n
    mede a força e a direção da relação linear entre duas variáveis. \n
    em outras palavras, mede o quanto xs e ys variam em conjunto, em relação às suas médias. \n
    A correlação é basicamente a covariância normalizada. \n
    Formula: \n
    Corr(X,Y) = Cov(X,Y) / (σx * σy) \n
    Onde: \n
    Cov(X,Y): covariância entre X e Y \n
    σx: desvio padrão de X \n
    σy: desvio padrão de Y \n

    Se uma aumenta quando a outra aumenta → correlação positiva.
    Se uma aumenta quando a outra diminui → correlação negativa.
    Se não existe padrão → correlação próxima de 0. \n

    O valor da correlação sempre está entre -1 e 1: \n
    +1 → relação perfeitamente positiva (ex.: altura em cm vs altura em metros). \n
    -1 → relação perfeitamente negativa (ex.: número de cigarros fumados vs expectativa de vida, em um modelo simplificado). \n
    0 → sem relação linear (ex.: número do sapato vs número da sorte). \n

    DIFERENÇA ENTRE CORRELAÇÃO E COVARIÂNCIA: \n
    Covariância: dá um número que pode ser grande, pequeno, positivo ou negativo, mas difícil de interpretar porque depende da escala. \n
    Correlação: padroniza o valor para ficar sempre entre -1 e 1, facilitando comparar. \n
    Exemplo: \n
    Se eu medir altura em cm, a covariância vai dar um valor grande. \n
    Se eu medir em m, o valor muda. \n
    Mas a correlação continua a mesma, porque é independente da escala.
    '''
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25

#TESTE REMOVENDO O OUTLIER 100
outlier = num_friends.index(100)    # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

daily_hours_good = [dm / 60 for dm in daily_minutes_good]

#Sem o outlier 100 a correlação é bem mais forte!
assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
assert 0.57 < correlation(num_friends_good, daily_hours_good) < 0.58
#endregion

#endregion

#print(median(num_friends))