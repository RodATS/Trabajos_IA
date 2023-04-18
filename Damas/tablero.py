from ficha import *
import copy as cp

          
class Tablero():
  player = 0  
  cpu = 0
  tablero = []

  def __init__(self, turno):
    matriz = []
    for i in range(8):
      matriz.append([])
      for j in range(8):
        matriz[i].append(0)

    self.tablero = matriz
    self.turno = turno

  def printTablero(self):
    for i in range(8):
                for j in range(8):
                    if self.tablero[i][j] == 0:
                        print("0", end=" ")
                    else:
                        print(self.tablero[i][j].jugador, end=" ")
                print()
    return self.tablero
  
  def __repr__(self):
    tab = ""
    for i in range(8):
                for j in range(8):
                    if self.tablero[i][j] == 0:
                        tab += "0 "
                    else:
                        tab += str(self.tablero[i][j].jugador) + " "
                tab += "\n"
    return tab
  
  def printTablero2(self):
    return self.tablero

  def returnTurno(self):
    return self.turno

  def cambiarTurno(self):
    if self.turno == "jugador":
      self.turno = "c"

    else:
      self.turno = "jugador"

  def colocarPiezas(self):

    for i in range(3):
      for j in range(i % 2, 8, 2):
        self.player+=1
        self.tablero[i][j] = Ficha(1, i, j, "abajo")

    for i in range(5, 8):
      for j in range(i % 2, 8, 2):
        self.cpu+=1
        self.tablero[i][j] = Ficha(2, i, j, "arriba")

  def buscarFicha(self, px, py):
    ficha = None
    return self.tablero[px][py]
    
         
  def moverFicha(self, px, py, dir):
    #print (self.tablero)
    pos = self.buscarFicha(px, py)
    if pos == 0:  
      print("no se encontro la ficha")
      return False
    if (self.turno == "jugador"):
      temp = cp.deepcopy(pos)
      if temp.moverD(dir): # aca retorna falso para cuando la maquina quiera hacer el movimiento
        print("jugador")
        if (self.tablero[temp.x][temp.y] == 0):
          self.tablero[temp.x][temp.y], self.tablero[px][py] = self.tablero[px][py], self.tablero[temp.x][temp.y]
          pos.mover(temp.x, temp.y)
          return True
        elif (self.tablero[temp.x][temp.y].jugador == 2):
          enemigo_x = temp.x
          enemigo_y = temp.y
          if temp.moverD(dir):
            if self.tablero[temp.x][temp.y] == 0:
              print("comer")
              enemigo = self.buscarFicha(enemigo_x, enemigo_y)
              self.tablero[enemigo.x][enemigo.y] = 0
              self.cpu-=1 #comemos la ficha
              self.tablero[px][py], self.tablero[temp.x][temp.y] = self.tablero[temp.x][temp.y], self.tablero[px][py]
              pos.mover(temp.x, temp.y)
              return True
          return False
      else: # no se puede mover
        return False
    else:
      temp = cp.deepcopy(pos)
      if temp.moverD(dir):
        print("jugador")
        if (self.tablero[temp.x][temp.y] == 0):
          self.tablero[temp.x][temp.y], self.tablero[px][py] = self.tablero[px][py], self.tablero[temp.x][temp.y]
          pos.mover(temp.x, temp.y)
          return True
        elif (self.tablero[temp.x][temp.y].jugador == 1):
          enemigo_x = temp.x
          enemigo_y = temp.y
          if temp.moverD(dir):
            if self.tablero[temp.x][temp.y] == 0:
              print("comer")
              enemigo = self.buscarFicha(enemigo_x, enemigo_y)
              #print(self.tablero[enemigo_x][enemigo_y],self.player,"enemigo")
              self.tablero[enemigo.x][enemigo.y] = 0
              self.player-=1
              self.tablero[px][py], self.tablero[temp.x][temp.y] = self.tablero[temp.x][temp.y], self.tablero[px][py]
              pos.mover(temp.x, temp.y)
              return True
      else:
        return False

  def ganador(self):
    if (self.player == 0):
      return "cpu"
    elif (self.cpu == 0):
      return "jugador"
    else:
      return False
  
  def puntaje(self):
    return self.cpu - self.player
