can_Numeros = (0,52,1,20,1,16,2,48,3,32,5,72,8,52,13,99,21,75,34,49,55,110,89,71,144)
v=1
listaFN = []
listaBA = []
def mostrarLinea(lista):
   for valores in lista:
        print(valores, end=" ") 
    
  
print("\n                     Lista de numeros: \n")
mostrarLinea(can_Numeros)
print("\n")
for valores in can_Numeros:
    if v == 1:
        listaFN.append(valores)
    elif v % 2 == 1:
        listaFN.append(valores)
    else:
        listaBA.append(valores)
    
    v += 1
 
print("       Listas Arregladas\n")
print("Sucesiones Fibonacci: ", end="")
mostrarLinea(listaFN)
print("\nCantidades Basura: ", end="")
mostrarLinea(listaBA)
print("\n")

