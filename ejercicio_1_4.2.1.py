import numpy
import random
matriz=numpy.diag([1,1,1])
for i in range(3):
    for j in range(3):
        matriz[i][j]=random.randint(0,100)
print(matriz)

















'''import numpy
arreglo_bi=numpy.array([[1,2,3],[4,5,6]])
for i in range(2):
    for j in range(3):
        print(arreglo_bi[i,j])
print(".............")
print(arreglo_bi[1][1])
'''