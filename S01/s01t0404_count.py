# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack','Raziel','Omar','Patoclo','Pancracio'] # O(1).

def random_function(students):
    first = students[0] # 0(1).
    total = 0 # 0(1).
    new_list = [] # 0(1).
    for student in students:
        print("Se le suma 1 a total")
        total += 1 # 0(n)
        new_list.append(student) # 0(n).

    print("Imprimiendo estudiantes")
    print(new_list) # 0(1).
    return total # 0(1).

print(f"tamaño de lista:{len(student_list_01)}")
print(random_function(student_list_01))
print("")

# Calcular 0(2n)+O(5)=0(2n+5)=0(n)
"""
0(3n+5)= O(3n) =0(n)
resultado final O=(n)
"""