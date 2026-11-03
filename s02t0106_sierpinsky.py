from array import array as arr #El primer array es una biblioteca, el segundo modulo y el tercero lo tomamos
#como la herramientra y la renombro a arr
from enum import Enum

# Borra pantalla con caracteres ANSI
def clear_screen():
    print("\033[2J\033[H", end="")

# Encapsulado de los valores ANSI para colores en un enumerado
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# Función para imprimir matriz
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Función para generar triángulo
def generate_triangle(rows = 1):
    columns = 2 * rows - 1
    matrix = []
    
    # Construyendo el grid (retícula)
    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matrix.append(new_row)
        
    # Calculando el centro de la primera fila
    center = columns // 2
    matrix[0][center] = 1

    # Se calcula el resto de la matriz siguiendo la lógica del triángulo de Sierpinski
    for row in range(1, rows):
        for col in range(0, columns):
            left_upper_cell = 0
            right_upper_cell = 0
            
            # Si la columna es mayor a cero
            if col > 0:
                left_upper_cell = matrix[row - 1][col - 1]
            # Si la columna está antes del borde derecho
            if col < columns - 1:
                right_upper_cell = matrix[row - 1][col + 1]
                
            # Lógica de las celdas vecinas (Sierpinski)
            if left_upper_cell != right_upper_cell:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
                
    return matrix

# Dibuja la matriz
def draw_matrix(input_matrix, symbol="■"):
    for row in input_matrix: 
        for cell in row:
            if cell == 1:
                print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value, end="")
            else:
                print(AnsiColor.RED.value + " ", end="")
        print()  # <--- CORRECCIÓN: Salto de línea necesario al terminar cada fila

# Método principal
def main():
    # CORRECCIÓN: Se ajustó a 8 filas para que coincida con la imagen
    matrix = generate_triangle(8)
    # Limpia la pantalla antes de dibujar la matriz
    clear_screen()
    # Dibuja la matriz en pantalla
    draw_matrix(matrix, symbol="■")

if __name__ == "__main__":
    main()