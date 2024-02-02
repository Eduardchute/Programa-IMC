
# ¿Qué construirás?   

# Crear un programa que pida al usuario su NOMBRE, APELLIDO PATERNO, APELLIDO MATERNO, EDAD, PESO y ESTATURA, 
# DESPLEGARLOS en pantalla junto con su Índice de Masa Corporal (IMC).
# El programa NO puede permitir que ningún dato quede vacío, 
# además de asegurarse de que en los campos de edad, peso y estatura el usuario introduzca una cifra. 
# Todo esto antes de proceder con el cálculo del IMC siguiendo la fórmula:
# Peso / estatura2   -> Peso sobre estatura al cuadrado


# Datos de Usuario

nombre = input('Ingrese su nombre completo: ')

cond = False  
while cond == False:
    try:
        edad = input('Ingresa su edad: ')
        if edad is not None:   # para no dejar espacios vacios
            edad = float(edad)
            cond = True
        else:
            print('Ingresa un dato no nulo')
    except ValueError:
        print('Por favor, ingresa un valor númerico')


cond1 = False  
while cond1 == False:
    try:
        peso = input('Ingresa su peso en kilogramos: ')
        if peso is not None:   # para no dejar espacios vacios
            peso = float(peso)
            cond1 = True
        else:
            print('Ingresa un dato no nulo')
    except ValueError:
        print('Por favor, ingresa un valor númerico')

cond2 = False  
while cond2 == False:
    try:
        estatura = input('Ingresa su estatura en metros: ')
        if estatura is not None:   # para no dejar espacios vacios
            estatura = float(estatura)
            cond2 = True
        else:
            print('Ingresa un dato no nulo')
    except ValueError:
        print('Por favor, ingresa un valor númerico')

imc = peso / estatura ** 2

print('Hola, ', nombre, 'tu edad es de', edad, 'años, ', 'tu peso es de ', peso, 'kilos,', 
      'tu estatura de', estatura, 'metros','dando un Indice de masa corporal de: ', imc)



