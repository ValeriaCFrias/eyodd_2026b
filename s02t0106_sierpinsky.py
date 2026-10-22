from array import array as arr #El primer array es una biblioteca, el segundo modulo y el tercero lo tomamos
#como la herramientra y la renombro a arr
#Paramestros de mi cuadricula
rows=8
columns= 2*rows-1

#Creando la reticula 2D
matrix=[]
#Empezamos agregando una lista y le vamos agregando las filas
#Contruyendo elk grid (reticula)
for _ in range(rows):
    new_row=arr('i',[0]* columns) #Creamos nuevas filas con columnas llenas
    #de ceros dependiendo de que numero le pongamos, ejemplo, i le ponemos 6, nos dará [0,0,0,0,0,0]
    matrix.append(new_row)
#Validando la construcción del grid
print(f"Cantidad de filas:{len(matrix)}")
print(f"cantidad de columnas:{len(matrix[0])}")
for row in matrix:
    print(list(row))