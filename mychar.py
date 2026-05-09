# ------------------------------ 
# Script: mychar.py
# Descripción: Devuelve la cadena más larga de una lista de cadenas 
# Autor: Gabriel Rodríguez Hernández
# Fecha: 15 de noviembre de 2025 
# ------------------------------ 

def cadena_mas_larga(lista):
    
    """
    Recibe una lista de cadenas y devuelve la cadena más larga.
    Si hay varias con la misma longitud máxima, devuelve la primera alfabéticamente.
    Si la lista está vacía, devuelve una cadena vacía.
    """

    if lista == []:
        return ""
    
    mas_larga = lista[0]
    for palabra in lista:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
        elif len(palabra) == len(mas_larga):
            # si tienen la misma longitud, quedarse con la primera alfabéticamente
            if palabra < mas_larga:
                mas_larga = palabra
    return mas_larga

# programa principal
palabras = []
print("Introduce 5 palabras:")
palabras.append(input("Palabra 1: "))
palabras.append(input("Palabra 2: "))
palabras.append(input("Palabra 3: "))
palabras.append(input("Palabra 4: "))
palabras.append(input("Palabra 5: "))

resultado = cadena_mas_larga(palabras)
print("La palabra más larga es:", resultado)