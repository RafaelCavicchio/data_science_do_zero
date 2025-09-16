#Álgebra Linear ramo da matemática que calcula espaços vetoriais

from typing import List

Vector = List[float]

height_weight_age = [70, #polegadas
                     170, #libras
                     40] #anos
grades = [95, #teste1
          80, #teste2
          75, #teste3
          62] #teste4

def add(v: Vector, w: Vector) -> Vector:
    """Soma os elementos correspondentes"""
    assert len(v) == len(w), "vetores devem ser do mesmo comprimento"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1,2,3], [4,5,6]) == [5,7,9]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtrai os elementos correspondentes"""
    assert len(v) == len(w), "vetores devem ser do mesmo comprimento"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5,7,9], [4,5,6]) == [1,2,3]

def vector_sum(Vectors: List[Vector]) -> Vector:
    """Soma todos os elementos correspondentes"""
    #verifica se os vetores não estão vazios
    assert Vectors, "não pode somar vetores vazios"

    #verificque se os vetores são do mesmo tamanho
    num_elements = len(Vectors[0])
    assert all(len(v) == num_elements for v in Vectors), "vetores devem ser do mesmo comprimento"

    #o elemento de Nº i do resultado é a soma de todo vector[i]
    return [sum(vector[i] for vector in Vectors) for i in range(num_elements)]

assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16,20]

def multiplicar_escalar(c: float, v: Vector) -> Vector :
    '''Multiplica cada elemento do vetor por c'''
    return [c * v_i for v_i in v]

assert multiplicar_escalar(2, [1,2,3]) == [2,4,6]

def media_vetores(vectors = List[Vector]) -> Vector:
    '''Calcula a média de uma lista de vetores'''
    n = len(vectors)
    return multiplicar_escalar(1/n, vector_sum(vectors))

assert media_vetores([[1,2], [3,4], [5,6]]) == [3,4]