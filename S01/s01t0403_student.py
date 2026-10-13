'''
#1.Identifico el tamaño de la entrada "n"
#El tamaño de la entrada es el nmumero de estudiantes.
#2. Es ver cuanto crece el num de operaciones en el
# algoritmo conforme crece el tamaño de la entrada.
#Agrego las big0 identicadas.
#Teniendo en cuenta la cota superior  asintotica.
#0(n)+4*0(1)=0(n+4)=0(n)
'''

#creando una lista de estudiantes.
student_list=['Patricio','Raziel','Susana','Paula']
student_list_02=['Maximiliano','Bruno','Mateo','Emiliano']
#verificando precencia de estudiante.
def check_student(input_student,student_list):
    for student in student_list:
        if input_student==student:
            print("Estudiante encontrado ✅")
            return student
        #Si no encuentro al estudiante
        print("Estudiante no encontrado ❌")
        return None
#Probando algoritmo
check_student("Patroclo",student_list)