import numpy
matriz=numpy.zeros((3,3), dtype=int)
cont=1
for i in range(3):
    for j in range(3):
        if i==j:
            matriz[i][j]=cont
            cont+=1
print(matriz)