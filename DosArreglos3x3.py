import numpy
import random
matriz_a=numpy.zeros((3,3), dtype=int)
matriz_b=numpy.zeros((3,3), dtype=int)
for i in range(3):
    for j in range(3):
        matriz_a[i][j]=random.randint(0,100)
        matriz_b[i][j]=random.randint(0,100)
print(matriz_a)
print(matriz_b)
multi=matriz_a*matriz_b
print(multi)
