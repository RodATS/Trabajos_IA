import pygame, sys
from pygame.locals import *
from tablero import *
import copy as cp
from arbol import *

#TODO: corregir árbol
#TODO: permitir ingresar profundidad de árbol
def encontrarPiezas(tablero, jugador):
    piezas = []
    for i in range(8):
      for j in range(8):
        if (tablero.tablero[i][j] != 0):
          if (tablero.tablero[i][j].jugador == jugador):
            piezas.append(tablero.tablero[i][j])
    return piezas

class grafics():

  def __init__(self):
    pygame.init()
    self.screen_width = 640
    self.screen_height = 640
    self.screen = pygame.display.set_mode(
      (self.screen_width, self.screen_height))
    self.square_size = 80

  def drawFicha(self, matrix, screen):
    color_player1 = (255, 0, 0)  # rojo
    color_player2 = (0, 0, 255)  # azul
    for row in range(8):
      for col in range(8):
        x = col * self.square_size + self.square_size // 2
        y = row * self.square_size + self.square_size // 2
        if matrix[row][col] == 0:
          continue
        elif matrix[row][col].jugador == 1:
          pygame.draw.circle(screen, color_player1, (x, y),
                             self.square_size // 3)
        elif matrix[row][col].jugador == 2:
          pygame.draw.circle(screen, color_player2, (x, y),
                             self.square_size // 3)

  def doubleClick(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and not self.mouse_clicked:
      self.click_count += 1
      if event.button == 1:  # Botón izquierdo
        if self.click_count == 1:
          self.first_click_pos = pygame.mouse.get_pos()

        elif self.click_count == 2:
          self.second_click_pos = pygame.mouse.get_pos()
          self.first_click_pos = [
            int(self.first_click_pos[0] / 80),
            int(self.first_click_pos[1] / 80)
          ]
          self.second_click_pos = [
            int(self.second_click_pos[0] / 80),
            int(self.second_click_pos[1] / 80)
          ]
          print("Posición del primer clic:", self.first_click_pos)
          print("Posición del segundo clic:", self.second_click_pos)

          self.click_count = -1
          return True

      self.mouse_clicked = True

    elif event.type == pygame.MOUSEBUTTONUP and self.mouse_clicked:
      self.mouse_clicked = False
      return False

    return False

  def drawTablero(self, profundidad):

      background_color = (255, 255, 255)
      color1 = (230, 224, 153)  # blanco
      color2 = (151, 101, 44)  # negro
      tab = Tablero("c")
      tab.colocarPiezas()
      player_p = encontrarPiezas(tab, 1)
      cpu_p = encontrarPiezas(tab,2)
      self.mouse_clicked = False

      self.click_count = 0
      self.first_click_pos = None
      self.second_click_pos = None
      self.moveF = None
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()

        # Dibuja el fondo
        self.screen.fill(background_color)

        # Dibuja la cuadrícula
        for row in range(8):
          for col in range(8):
            x = col * self.square_size
            y = row * self.square_size
            color = color1 if (row + col) % 2 == 0 else color2
            pygame.draw.rect(self.screen, color,
                            (x, y, self.square_size, self.square_size))

        moveF = self.doubleClick(event)
        if (tab.turno == "jugador" and moveF):
          # tab = minimax(tab, 3, False, -10000, 10000)[1] #minimax, el número de pasos hacia adelante se tiene que definir
          # print("cambio de turno")
          # tab.cambiarTurno()
          for f in player_p:
            print(f.x, f.y)
          if ((self.first_click_pos[0] - self.second_click_pos[0]) % 2 or (abs(self.first_click_pos[0] - self.second_click_pos[0]) == 2)):
          #jugador
          
            if (self.first_click_pos[0] < self.second_click_pos[0]):
              if tab.moverFicha(self.first_click_pos[1], self.first_click_pos[0],
                            "D"):
                tab.cambiarTurno()
                print("cambio de turno")

            elif (self.first_click_pos[0] > self.second_click_pos[0]):
              if tab.moverFicha(self.first_click_pos[1], self.first_click_pos[0],
                            "I"):
                tab.cambiarTurno()
                print("cambio de turno")
            #tab.printTablero()
            self.first_click_pos = None
            self.second_click_pos = None

          #cpu
        elif (tab.turno == "c"):
    
          raiz = node(tab.tablero)
          tab = minimax(tab, profundidad, True, -10000, 10000, raiz)[1] #minimax, el número de pasos hacia adelante se tiene que definir
          raiz.printnode()
          
          print(tab.player, tab.cpu)
          print("cambio de turno")
          tab.cambiarTurno()
          # if (self.first_click_pos[0] < self.second_click_pos[0]):
          #   if tab.moverFicha(self.first_click_pos[1], self.first_click_pos[0],
          #                    "D"):
          #     tab.cambiarTurno()
          #     print("cambio de turno")

          # elif (self.first_click_pos[0] > self.second_click_pos[0]):
          #   if tab.moverFicha(self.first_click_pos[1], self.first_click_pos[0],
          #                    "I"):
          #     tab.cambiarTurno()
          #     print("cambio de turno")

          #tab.printTablero()
          self.first_click_pos = None
          self.second_click_pos = None


        matrix = tab.printTablero2()
        self.drawFicha(matrix, self.screen)

        pygame.display.update()

def posiblesMovimientos(pos, jug):
  mov = []
  player_p = encontrarPiezas(pos,  1)
  cpu_p = encontrarPiezas(pos,  2)
  print(len(player_p), len(cpu_p))
  if (jug == "jugador"):
    for p in player_p:
      simulation = cp.deepcopy(pos)
      simulation.turno = "jugador"
      if (simulation.moverFicha(p.x, p.y, "D")):
        print(simulation.player, simulation.cpu)
        mov.append(simulation)
        #simulation.printTablero()
      simulation2 = cp.deepcopy(pos)
      simulation2.turno = "jugador"
      if (simulation2.moverFicha(p.x, p.y, "I")):
        print(simulation2.player, simulation2.cpu)
        mov.append(simulation2)
        #simulation2.printTablero()
  else:
    for p in cpu_p:
      simulation = cp.deepcopy(pos)
      simulation.turno = "c"
      if (simulation.moverFicha(p.x, p.y, "D")):
        print(simulation.player, simulation.cpu)
        mov.append(simulation)
        #simulation.printTablero()
      simulation2 = cp.deepcopy(pos)
      simulation2.turno = "c"
      if (simulation2.moverFicha(p.x, p.y, "I")):
        print(simulation2.player, simulation2.cpu)
        mov.append(simulation2)
        #simulation2.printTablero()

  print("movimientos posibles: ", len(mov))
  return mov

def minimax(pos, depth, isMaximizing, alpha, beta, raiz):
  print ("minimax ", depth)
  if (depth == 0 or pos.ganador()):
    return pos.puntaje(), pos

  if (isMaximizing):
    bestScore = -10000
    bestMov = None
    for mov in posiblesMovimientos(pos, "pc"):
      nuevo_nodo = cp.copy(raiz.insert(mov.tablero))
      score = minimax(mov, depth - 1, False, alpha, beta, nuevo_nodo)[0]
      bestScore = max(score, bestScore)
      alpha = max(alpha, score)
      if (beta <= alpha):
        break
      if (score == bestScore):
        bestMov = mov
    return bestScore, bestMov
  
  else:
    bestScore = 10000
    bestMov = None
    for mov in posiblesMovimientos(pos, "jugador"):
      nuevo_nodo = raiz.insert(mov.tablero)
      score = minimax(mov, depth - 1, True, alpha, beta, nuevo_nodo)[0]
      bestScore = min(score, bestScore)
      beta = min(beta, score)
      if (beta <= alpha):
        break
      if (score == bestScore):
        bestMov = mov
    return bestScore, bestMov

  
profundidad = 3
draw = grafics()
draw.drawTablero(profundidad)
