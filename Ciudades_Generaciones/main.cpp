import matplotlib.pyplot as plt
import random
import math




def distancia_euclidiana(punto1,punto2):
    n = len(punto1) #x,y
    suma_cuadrados = 0
    for i in range(n):
        suma_cuadrados += (punto1[i] - punto2[i])**2
    return math.sqrt(suma_cuadrados)


def cambioCaminos(caminos,bits):
  limite = len(caminos)-1
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

    
def encontrarLosCaminosMasCaros(costoCamino,generacionN):
    indiceMaximo1 = 0
    indiceMaximo2 = 0

    for i in range(1,len(costoCamino[generacionN])):
        if( costoCamino[generacionN][i] > costoCamino[generacionN][indiceMaximo1]):
            indiceMaximo1 = i
    

    for j in range(1,len(costoCamino[generacionN])):
        if( costoCamino[generacionN][j] > costoCamino[generacionN][indiceMaximo2] and costoCamino[generacionN][j] < indiceMaximo1):
            indiceMaximo2 = j
        
    return indiceMaximo1,indiceMaximo2



def encontrarCaminoMinimo(costoCamino,generacionN):
   
    indiceMinimo1 = 0

    for i in range(1,len(costoCamino[generacionN])):
        if( costoCamino[generacionN][i] < costoCamino[generacionN][indiceMinimo1]):
            indiceMinimo1 = i
    
    return indiceMinimo1



nCiudades = 6
#A B C D E 
#Hay 13
posCiudades = [[2,3],[3,4],[5,4],[5,2],[3,1],[6,1],[1,1],[2,1],[3,3],[1,5],[4,2],[9,1],[2,9]]


nGeneraciones = 2
ejexGeneraciones = []
for i in range(nGeneraciones):
    ejexGeneraciones.append(i)


#cambio
bitsCambio = []
for i in range (nCiudades+1):
        bitsCambio.append(random.sample(range(0,2),1))
print(bitsCambio)

def cambioBitsPorGeneracion(bitsCambio):
    print("Nuevos bits")
    for i in range (nCiudades+1):
        bitsCambio[i]=(random.sample(range(0,2),1))
    print(bitsCambio)



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



#generaciones = 10
for gen in range(nGeneraciones):
    print("generacion " + str(gen))
    prom = 0
    for i in range(len(caminos)):
        distancia = 0
        print("Para el camino "+ str(i+1))
        for j in range(nCiudades):
            distancia += distancia_euclidiana(posCiudades[caminos[i][j]], posCiudades[caminos[i][j+1]])
        print(distancia)
        print("\n")
        costoPorCamino[i].append(distancia)
        prom += distancia
    promedios.append(prom/len(caminos))

    #seleccionar los caminos mas costosos
    #posiciones de los caminos mas caros por generacion, inicilizacion
    pos1,pos2 = encontrarLosCaminosMasCaros(costoPorCamino,gen)

    print(pos1)
    print(pos2)

    print(costoPorCamino)
    # cambio en los caminos mas caros
    cambioCaminos(caminos[pos1],bitsCambio)
    cambioCaminos(caminos[pos2],bitsCambio)

    cambioBitsPorGeneracion(bitsCambio)
    

posMin = encontrarCaminoMinimo(costoPorCamino,nGeneraciones-1)

plt.plot(ejexGeneraciones,promedios, ":",color="b")
plt.plot(ejexGeneraciones, costoPorCamino[posMin],":",color="r")
plt.show()
