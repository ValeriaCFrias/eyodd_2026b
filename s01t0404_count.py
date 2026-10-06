# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # ?

def random_function(students):
    first = students[0] # 0(n)
    total = 0 # 0(1)
    new_list = [] # 0(1)

    for student in students:
        total += 1 # 0(1)
        new_list.append(student) # 0(1)

    print(new_list) # 0(n)
    return total # 0(1)

print(random_function(student_list_01))

# Calcular O(?)
"""
0(3n+5)= O(3n) =0(n)
"""