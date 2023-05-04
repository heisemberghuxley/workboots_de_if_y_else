#programa que recibe lista de palabras y solo muestra solo las que empiezan por determinada palabra


palabras = input("Ingrese una lista de palabras separadas por comas: ") 
lista_palabras = palabras.split(",") 
letra = input("Ingrese la letra determinada: ") 
for palabra in lista_palabras: 
    if palabra.startswith(letra): 
        print(palabra)