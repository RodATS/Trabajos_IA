import matplotlib.pyplot as plt
import random
import math


#promedios.append(random.sample(range(1,80),1))
#plt.plot(promedios,ejeyGeneraciones, ":",color="b")
#plt.show()


def distancia_euclidiana(punto1,punto2):
    n = len(punto1) #x,y
    suma_cuadrados = 0
    for i in range(n):
        suma_cuadrados += (punto1[i] - punto2[i])**2
    return math.sqrt(suma_cuadrados)


def partition(array, bits, low, high):
  pivot = bits[high][0]
  i = low - 1

  for j in range(low, high):
    if bits[j][0] > pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

# function to perform quicksort
def quickSort(array, bits, low, high):
  if low < high:

    pi = partition(array, bits, low, high)
    quickSort(array, bits, low, pi - 1)
    quickSort(array, bits, pi + 1, high)


def cambioCaminos(caminos,bits):
  limite = len(caminos)-1
  '''
  indexUno = 1
  indexCero = 1
  while(indexCero < limite and indexUno < limite):
    if(indexCero == indexUno and bits[indexCero][0] == 1 and bits[indexUno][0] == 1):
        indexCero += 1
        indexUno += 1
    elif(indexCero <= indexUno and bits[indexCero][0] == 0 and bits[indexUno][0] == 0):
      indexUno +=1
    elif(indexCero < indexUno and bits[indexCero][0] == 0 and bits[indexUno][0] == 1):
      temp = caminos[indexCero]
      caminos[indexCero] = caminos[indexUno]
      caminos[indexUno] = temp
      indexCero += 1
      indexUno += 1
  '''
  quickSort(caminos, bits, 1, limite -1)

    
def encontrarLosCaminosMasCaros(costoCamino,generacionN):
    indiceMaximo1 = 0
    indiceMaximo2 = 0
    indiceMinimo3 = 0
    indiceMinimo4 = 0

    for i in range(1,len(costoCamino)):
        if( costoCamino[i][generacionN] > costoCamino[indiceMaximo1][generacionN]):
            indiceMaximo1 = i
    

    for j in range(1,len(costoCamino)):
        if( costoCamino[j][generacionN] > costoCamino[indiceMaximo2][generacionN] and costoCamino[j][generacionN] < costoCamino[indiceMaximo1][generacionN] and indiceMaximo1 != j):
            indiceMaximo2 = j

    for i in range(1,len(costoCamino)):
        if( costoCamino[i][generacionN] < costoCamino[indiceMinimo3][generacionN] and i != indiceMaximo1 and i != indiceMaximo2 ):
            indiceMinimo3 = i
    

    for j in range(1,len(costoCamino)):
        if( costoCamino[j][generacionN] < costoCamino[indiceMinimo4][generacionN] and costoCamino[j][generacionN] > costoCamino[indiceMinimo3][generacionN] and j != indiceMinimo3 ):
            indiceMinimo4 = j
        
    return indiceMaximo1,indiceMaximo2,indiceMinimo3, indiceMinimo4



def encontrarCaminoMinimo(costoCamino,generacionN):
   
    indiceMinimo1 = 0

    for i in range(1,len(costoCamino)):
        if( costoCamino[i][generacionN] < costoCamino[indiceMinimo1][generacionN]):
            indiceMinimo1 = i
    
    return indiceMinimo1




nCiudades = 20
#A B C D E 
#Hay 13
posCiudades = [[2,3],[3,4],[5,4],[5,2],[3,1],[6,1],[1,1],[2,1],[3,3],[1,5],[4,2],[9,1],[2,9],[5,5],[1,9],[3,2],[6,7],[7,3],[6,6],[7,2]]


nGeneraciones = 100
ejexGeneraciones = []
for i in range(nGeneraciones):
    ejexGeneraciones.append(i)


#cambio
bitsCambio = []
for i in range (nCiudades+1):
        bitsCambio.append(random.sample(range(0,2),1))
#print(bitsCambio)

def cambioBitsPorGeneracion(bitsCambio):
    #print("Nuevos bits")
    for i in range (nCiudades+1):
        bitsCambio[i]=(random.sample(range(0,2),1))
    #print(bitsCambio)



#caminos iniciales: aleatorios
nCaminos = 4
caminos = []
for i in range (nCaminos):
    numeros_aleatorios = random.sample(range(1, nCiudades), nCiudades-1)
    numeros_aleatorios.insert(0,0)
    numeros_aleatorios.append(0)
    caminos.append(numeros_aleatorios)

#grafica para los promedios
promedios = []

#para la grafica de los mejores individuos (camino) durante las generaciones
costoPorCamino = [[],[],[],[]]


posMinIncio = 0
#generaciones = 10
for gen in range(nGeneraciones):
    print("generacion " + str(gen))
    prom = 0
    for i in range(len(caminos)):
        distancia = 0
        #print("Para el camino "+ str(i+1))
        for j in range(nCiudades):
            distancia += distancia_euclidiana(posCiudades[caminos[i][j]], posCiudades[caminos[i][j+1]])
        #print(distancia)
        #print("\n")
        costoPorCamino[i].append(distancia)
        prom += distancia
    promedios.append(prom/nCaminos)

    #seleccionar los caminos mas costosos
    #posiciones de los caminos mas caros, inicilizacion
    pos1,pos2, pos3, pos4 = encontrarLosCaminosMasCaros(costoPorCamino,gen)

    #posiciones de los caminos mas baratos, inicilizacion

    #print(costoPorCamino)
    #hacer la copia
    #caminos[pos1] = caminos[pos3]
    #caminos[pos2] = caminos[pos4]

    #print(pos1)
    #print(pos2)
    #print(pos3)
    #print(pos4)

    #print(costoPorCamino)
    # cambio en los caminos mas caros (copias)
    print(bitsCambio)
    cambioCaminos(caminos[pos1],bitsCambio)
    cambioCaminos(caminos[pos2],bitsCambio)

    cambioBitsPorGeneracion(bitsCambio)
    if(gen == 0):
        posMinIncio = encontrarCaminoMinimo(costoPorCamino,gen)
    

posMinFinal = encontrarCaminoMinimo(costoPorCamino,nGeneraciones-1)

print("\nDistancia del menor camino al inicio")
print(costoPorCamino[posMinIncio][nGeneraciones-1])
print("\nDistancia del menor camino al final")
print(costoPorCamino[posMinFinal][nGeneraciones-1])

print("Debería graficar pronto")
print("Debería graficar pronto")

plt.plot(ejexGeneraciones,promedios, ":",color="b")
plt.plot(ejexGeneraciones, costoPorCamino[posMinIncio],":",color="r")
plt.plot(ejexGeneraciones, costoPorCamino[posMinFinal],":",color="g")
plt.show()
