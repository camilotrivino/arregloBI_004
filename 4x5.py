import numpy
import random
matriz=numpy.zeros((4,5), dtype=int)
for i in range(4):
    for j in range(5):
        matriz[i][j]=random.randint(0,100)
print(matriz)
for y in range(4):
    cont_fila=0
    for x in range(5):
        cont_fila+=matriz[y][x]
    print(cont_fila)
print("----------")
for x in range(5):
    cont_columna=0
    for y in range(4):
        cont_columna+=matriz[y][x]
    print(cont_columna)

        
