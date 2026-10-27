from array import array as arr #El primer array es una biblioteca, el segundo modulo y el tercero lo tomamos
#como la herramientra y la renombro a arr
#Paramestros de mi cuadricula
rows=10
columns= 2*rows-1
#Funcion para imprimir matrix
def print_matrix(input_matrix):
    for row in input_matrix:
     print(list(row))
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
# for row in matrix:
    # print(list(row))
    #Calculando el centro de la primera fila.
center=columns //2 #Se hace la division
#Estableciendo el centro en 1
matrix[0][center]=1
#print_matrix(matrix)
#Se calcula el resto de la matrix
# siguiendo la logica del sierpinsky Gasket
for row in range(1,rows):
   for col in range(0,columns):
    left_upper_cell=0
    right_upper_cell=0
    #Si la columna donde estamos
    #es mayor a cero

    if col>0:
      left_upper_cell=matrix[row-1][col-1]
#si la columna de un elemento esta antes del borde derecho
   if col<columns-1:
     right_upper_cell=matrix[row-1][col+1]
   #guardo el arreglo
   if left_upper_cell!=right_upper_cell:
      matrix[row][col]=1
   else:
       matrix[row][col]=0

print()
print_matrix(matrix)
      
