# Longitud de una frase

# Crear un programa para identificar la longitud de una palabra ingresada. 
# La palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:
# Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, 
# se debe imprimir un mensaje que indique que la palabra es correcta
# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. 
# Solo tiene N letras (siendo N el número de letras de la palabra)
# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. 
# Tiene N letras ((siendo N el número de letras de la palabra))

def contar_letras(palabra, cond): # se define una función para que reciba los datos
    longitud = len(palabra) # Esta variable contabiliza la longitud (letras) de la palabra

# Con esta condicional se pone para que valla validando las opciones 

    if longitud < 4: # Por si la palabra es menor a 4 letras
        print (f'Hacen falta letras, solo tienes {longitud} letras.')

    elif 4 <= longitud <=8: # Por si la palabra cumple con la  cantidad de letras
        print ('Palabra correcta !!!')
        cond = False # si se cumple la condicional True cambia a False

    else: # Por si la palabra es mayor a 8 letras
        print (f'Sobran letras, Tiene {longitud} letras.')
    return cond

cond = True
while cond == True:
    palabra = input('Ingresa una palabra entre 4 y 8 caracteres: ')
    cond = contar_letras(palabra, cond)


# Crear un programa que en base a 2 números de entrada, coordenadas, 
# Identifique en cuál de los 4 cuadrantes se encuentra el punto
# Las coordenadas ubican un punto dentro del cuadrante el cual podemos encontrar por medio de sus valores. 
# Por ejemplo, en la siguiente gráfica, el punto rojo se encuentra en las coordenadas (-3, 2) 
# y esto ubica al punto dentro del cuadrante II. Por otro lado, el punto azul se ubica en (-1, 1) 
# ubicándolo en el cuadrante IV


def encontrar_cuadrante(x,y):
    if x > 0 and y > 0:
       print (f'la cordenada ({x},{y}) pertenecen al cuadrante I')
    elif x < 0 and y > 0:
        print (f'la cordenada ({x},{y}) pertenecen al cuadrante II')
    elif x < 0 and y < 0:
        print (f'la cordenada ({x},{y}) pertenecen al cuadrante III')
    elif x > 0 and y < 0:
        print (f'la cordenada ({x},{y}) pertenecen al cuadrante IV')
    elif x == 0 and y != 0:
        print (f'la cordenada ({x},{y}) pertenece al eje de Y')
    elif x != 0 and y == 0 :
        print (f'la cordenada ({x},{y}) pertenece al eje de X')
    else:
        print (f'la cordenada ({x},{y}) pertenece al Origen')

encontrar_cuadrante(8,0)
