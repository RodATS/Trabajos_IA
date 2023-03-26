import pygame, sys
from pygame.locals import DOUBLEBUF
from pygame.locals import QUIT
from numpy import ones
from numpy import zeros  
import random
from collections import deque


'''
TODO:
    Añadir nodo del medio (adiós performance)
    Arreglar DFS
  	Programar BFS (1 a 1)
	(opcional) Programar crecimiento de la matriz dinámico
'''

'''
Objects
'''
class Button():
    def __init__(self, x, y, width, height, color, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': "#"+color,
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        DISPLAYSURF.blit(self.buttonSurface, self.buttonRect)
            
pygame.init()
     
'''
Globals
'''
fps = 15
fpsClock = pygame.time.Clock()
flags = DOUBLEBUF
DISPLAYSURF = pygame.display.set_mode((1280, 750), flags, 16)
font = pygame.font.SysFont('Arial', 40)
objects = [] #objects in display
r = c = 5 #dimensions of graph

nodes = []
edges = [(0,1)]
nodePositions = [(120,100)]
node_size = 2
drawedNodes = []
num_nodes = 0


camino = []
nodo_ini =0
nodo_switch = True
nodo_fin = 0

coloredNodes = []

'''
Functions
'''

def drawNode(posx, posy, size, color):
	n = pygame.draw.circle(DISPLAYSURF, color, (posx, posy), size)
	return n

def drawEdge(node1, node2):
	pygame.draw.line(DISPLAYSURF,[150,205,205], node1.center, node2.center)

def drawGraph():
    global drawedNodes
    drawedNodes = []
    
    for i in range(0,len(nodes)):
      if (nodes[i]):
        drawedNodes.append(drawNode(nodePositions[i][0],nodePositions[i][1],node_size,[187,255,255]))
      else: 
        drawedNodes.append(None)
        
    r = len(edges[0])
    for j in range(0,len(edges)):
      for k in range(0,r):
        if (edges[j][k]):
          drawEdge(drawedNodes[j], drawedNodes[k])

         
def makeGraph(size):
    global nodes 
    nodes = range(0,size)
    global edges 
    edges = [(i, i + 1) for i in range(size - 1)]
    global nodePositions
    nodePositions = [(i*100+20,100)for i in range(size)]

def makeGridGraph(rows,cols):
    num_nodes = rows * cols

    global nodes 
    nodes = ones(num_nodes)
    global edges 
    edges = zeros((num_nodes, num_nodes))
    for i in range(0,num_nodes):
        if((i+1) % cols > 0):
            if(i+1 + cols <= num_nodes):
                edges[i][i+1] = 1
                edges[i][i+cols] = 1
                edges[i][i+cols+1] = 1
            else:
                edges[i][i+1] = 1
        else:
            if(i+1 + cols <= num_nodes):
                edges[i][i+cols] = 1
        if(i % cols > 0):
            if(i+1 + cols <= num_nodes):
                edges[i][i+cols-1] = 1

    space_size_h = 1280 / cols
    space_size_v = 720 / rows
    
    if space_size_h < 14:
        space_size_h = 14
    if space_size_v < 9:
        space_size_v = 9

    global node_size
    node_size = space_size_h / 7
    edge_size_h = space_size_h - node_size
    edge_size_v = space_size_v - node_size
    
    global nodePositions
    nodePositions.clear() 
    for i in range(0, rows): # estos for y el de arriba se podrían combinar
        for j in range(0, cols):
            nodePositions.append((j*edge_size_h + node_size, i*edge_size_v + node_size))
    
def eraseNode(n,numnodes):
  if (nodes[n]):
    edges[n,:] = zeros((1,numnodes))
    edges[:,n] = zeros(numnodes)
    nodes[n] = 0
    global num_nodes
    num_nodes -= 1

def dfs():
    visited =[False] * c*r #for DFS
    global nodo_ini
    global nodo_fin
    if(nodo_ini > nodo_fin):
        temp=nodo_fin
        nodo_fin = nodo_ini
        nodo_ini = temp
    print("ini: ",nodo_ini)
    print("fin: ",nodo_fin)
    stack = deque()
    stack.append(nodo_ini)
    # Bucle # hasta que la stack esté vacía
    while stack:
        ini = stack.pop()
        #si el vertice fue borrado, valor 0
        if nodes[ini] == 0:
            continue
        # si el vértice ya está descubierto, ignóralo
        if visited[ini]:
            continue
        visited[ini] = True
        camino.append(ini)
        drawNode(drawedNodes[ini].x + node_size, drawedNodes[ini].y + node_size,node_size,(255,0,0))
        pygame.display.update(drawedNodes[ini])
        coloredNodes.append(ini)#to clear it later
        # si llega al objetivo
        if ini == nodo_fin:
            return
        adjList = edges[ini]
        for i in reversed(range(len(adjList))):
            if adjList[i] == 0:
                continue
            if not visited[i]:
                stack.append(i)


def BFS():
  visited =[False] * c*r #for BFS
  global nodo_ini
  global nodo_fin
  if(nodo_ini > nodo_fin):
        temp=nodo_fin
        nodo_fin = nodo_ini
        nodo_ini = temp
  print("ini: ",nodo_ini)
  print("fin: ",nodo_fin)
  stack = deque()
  stack.append(nodo_ini)
  visited[nodo_ini] = True
  
  while stack:
    ini = stack.pop()
    if nodes[ini] == 0:
      continue
    
    print(ini, end = " ")
    camino.append(ini)
    drawNode(drawedNodes[ini].x + node_size, drawedNodes[ini].y + node_size,node_size,(255,0,0))
    pygame.display.update(drawedNodes[ini])
    coloredNodes.append(ini)#to clear it later
    if ini == nodo_fin:
      return
    adjList = edges[ini]
    for ng in reversed(range(len(adjList))):
      if visited[ng] == 0:
        visited[ng] = True
        stack.append(ng)
    

def reduceNodes(perc):
    #borrar un porcentaje de nodos aleatorios
    numnodes = num_nodes
    DISPLAYSURF.fill((20, 20, 20))
    while (num_nodes > (numnodes-(r*c*perc)//100)):
        eraseNode(random.randint(0,r*c-1),r*c)
    drawGraph()
    pygame.display.update()

def buttonFunction100():
    print("Loading 100 graph")
    makeGridGraph(r, c)
    reduceNodes(0)
    
def buttonFunction70():
    print("Loading 70 graph")
    makeGridGraph(r, c)
    reduceNodes(30)

def buttonFunction50():
    print("Loading 50 graph")
    makeGridGraph(r, c)
    reduceNodes(50)
    
def buttonFunction30():
    print("Loading 30 graph")
    makeGridGraph(r, c)
    reduceNodes(70)

def detectClickOnNode():
    global nodo_ini
    global nodo_switch
    global camino
    mousePos = pygame.mouse.get_pos()
    for i in range(0,len(drawedNodes)):
        if drawedNodes[i] is not None:
            if drawedNodes[i].collidepoint(mousePos):
                #pygame.event.get()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if nodo_switch == True:
                        clearNodes()
                        
                        drawNode(drawedNodes[i].x + (node_size),drawedNodes[i].y + (node_size),node_size,[0,0,0])
                        pygame.display.update(drawedNodes[i])
                        coloredNodes.append(i)
                        pygame.time.wait(200)
                        
                        nodo_ini = i
                        nodo_switch = False
                        
                    else:
                        drawNode(drawedNodes[i].x + (node_size),drawedNodes[i].y + (node_size),node_size,[0,0,0])
                        pygame.display.update(drawedNodes[i])
                        coloredNodes.append(i)
                        pygame.time.wait(200)
                        global nodo_fin
                        nodo_fin = i
                        # BFS(nodo_ini,nodo_fin)
                        print(camino)
                        camino = []
                        nodo_switch = True

def clearNodes():
    print(coloredNodes)
    for i in coloredNodes:
        if drawedNodes[i] is not None:
            drawNode(drawedNodes[i].x + node_size,drawedNodes[i].y + node_size,node_size,[187,255,255])
            pygame.display.update(drawedNodes[i])
    coloredNodes.clear()
    

Button(1170, 30, 100, 50, "CDC8B1", "100%",  buttonFunction100, True)
Button(1170, 130, 100, 50, "CDC8B1", "70%",  buttonFunction70, True)
Button(1170, 230, 100, 50, "CDC8B1", "50%",  buttonFunction50, True)
Button(1170, 330, 100, 50, "CDC8B1", "30%",  buttonFunction30, True)
Button(1170, 500, 100, 50, "556B2F", "DFS",  dfs, True)
Button(1170, 600, 100, 50, "556B2F", "BFS",  BFS, True)
botones = ((1170, 30, 100, 50),(1170, 130, 100, 50),(1170, 230, 100, 50),(1170, 330, 100, 50),(1170, 500, 100, 50),(1170, 600, 100, 50))

DISPLAYSURF.fill((20, 20, 20))
makeGridGraph(r,c)
reduceNodes(30)
drawGraph()
pygame.display.update()


while nodes[nodo_ini] == 0:
    nodo_ini+=1

#dfs(nodo_ini, camino)
#print(camino)

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for object in objects:
		object.process()
	detectClickOnNode()
	pygame.display.update(botones)
	fpsClock.tick(fps)
	
	
