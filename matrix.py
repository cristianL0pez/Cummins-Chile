matriz = [
[1,2,3,4],     
[5,6,7,8],
[9,10,11,12],
[13,14,15,16] 
]

for column in range(len(matriz[0])):
    for fila in range(len(matriz)):
        if column%2==0:
            print(matriz[fila][column])
        else:
            print(matriz[~fila][column])
            