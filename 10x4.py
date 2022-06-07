import numpy
import random
acumulador=0
matriz_a=numpy.zeros((10,4), dtype=int)
for i in range(10):
    for j in range(4):
        acumulador+=1
        matriz_a[i][j]=acumulador
print(matriz_a)