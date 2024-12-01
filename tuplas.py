#TUPLA
numeros = (1,2,3,4,5) #crea la tupla
print(numeros[-2]) #imprime

numeros = (1,2,3,4,5,6,7,8,9,10)
for numero in numeros:
   print(numero)

for indice, numero in enumerate(numeros):
   print("El elemento en el índice"+str(indice)+" es " +str(numero))

for indice, numero in enumerate(numeros):
   print("El resultado de "+str(numero)+ " * "+str((indice+1))+" es : "+str((numero*(indice+1))))

paises=("Mexico","Guatemala","Honduras","Panama","Belice") #crea la tupla
for palabra in paises:
    print(palabra) #recorre e imprime la tupla

paisNuevo=input("Digite un país:")
for letra in paisNuevo:
   print(letra)

paises=("Mexico","Guatemala","Honduras","Panama","Belice") 
for palabra in paises:
   for letra in palabra:
    print(letra) 

#Longitud de tupla

#Buscar un valor en una tupla
libros = ("cementerio de mascotas", "it","la cupula", "hush")
libro = input("Digite un libro: ").lower()
if libro in libros:
   print("Si contamos con el libro",libro,"puede comprarlo")
else:
   print("No tenemos ese libro")
