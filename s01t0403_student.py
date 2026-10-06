#creando una lista de estudiantes
'''
NOTAS
1.Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.
2.Es ver cuanto crece el numero de operaciones
en mi algoritmo conforme crece el tamaño de la entrada
agrego las bigO identicas, teniendo en cuenta la Cota
superior asintotica
O(n) + O(4) = O(n+4) = O(n)
'''
student_list_01 = ['jordan','oscar','jose','pepe']
student_list_02 = ["mario","ale","maria","sofia"]


def check_student(input_student, student_list):
    for student in student_list:
     if input_student == student: #O(n)
        print("✅ Estudiante encontrado")#O(1)
        return student #O(1)
#si no encuentro al estudiante
    print("❌ Estudiante no encontrado")#O1
    return None
# Probando algoritmo
check_student("oscar",student_list_01)