
import pygame, sys, pygame_textinput
from pygame.locals import DOUBLEBUF
from pygame.locals import QUIT
from scipy.spatial import distance
import heapq
'''
	TODO:
 		- Algoritmo A*
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
inf = 999999
fpsClock = pygame.time.Clock()
flags = DOUBLEBUF
DISPLAYSURF = pygame.display.set_mode((1280, 720), flags, 16)
font = pygame.font.SysFont('Arial', 40)
objects = [] #objects in display


coloredNodes = []
nodo_switch = True
nodo_inicio = None
nodo_fin = None

ini_range = None
fin_range = None

node_size = 2
dim = (10,10)  #row,col
num_nodes = dim[0]*dim[1]

class node:
    def __init__(self,name,pos):
        self.name = name
        self.pos = pos
        self.active = True
        self.circle = None
        self.color = (0,0,255)
    def __str__(self):
        return f"{self.name}({self.pos})"
    def drawNode(self):
        if self.active:
            self.circle = pygame.draw.circle(DISPLAYSURF,self.color,self.pos,node_size)
        
    def deactivate(self):
        self.active = False

class matAdy:
    def __init__(self):
        self.mat = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        self.color = (0,0,255)
    def __str__(self):
        str = []
        for i in self.mat:
            for j in i:
                str.append(j)
            str.append("|")
        return f"{str}"
    def addEdge(self,node1, node2):
        if nodes[node1].active and nodes[node2].active:
            self.mat[node1][node2] = 1
            self.mat[node2][node1] = 1
    def drawEdges(self):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i <= j and self.mat[i][j] == 1:
                    pygame.draw.line(
                        DISPLAYSURF,self.color,nodes[i].pos,nodes[j].pos)

def drawNodes(nodes):
    for i in nodes:
        i.drawNode()
    
def generateNodes():
    h,v = makelimits()
    nodes = list(range(0,num_nodes))
    for i in range(0,dim[0]):
        for j in range(0,dim[1]):
            nodes[(dim[0]*i)+j] = node(
                (dim[0]*i)+j, (i*h + node_size,j*v + node_size) )
    return nodes

def generateEdges():
    for i in range(0,num_nodes):
        if nodes[i].active:
            if((i+1) % dim[1] > 0):
                if(i+1 + dim[1] <= num_nodes):
                    mAdy.addEdge(i,i+1)
                    mAdy.addEdge(i,i+dim[1])
                    mAdy.addEdge(i,i+dim[1]+1)
                else:
                    mAdy.addEdge(i,i+1)
            else:
                if(i+1 + dim[1] <= num_nodes):
                    mAdy.addEdge(i,i+dim[1])
            if(i % dim[1] > 0):
                if(i+1 + dim[1] <= num_nodes):
                    mAdy.addEdge(i,i+dim[1]-1)

   
def makelimits():
    space_size_h = 1280 / dim[0]
    space_size_v = 720 / dim[1]
    
    if space_size_h < 14:
        space_size_h = 14
    if space_size_v < 9:
        space_size_v = 9

    global node_size
    node_size = space_size_h / 7
    edge_size_h = space_size_h - node_size
    edge_size_v = space_size_v - node_size
    
    return edge_size_h, edge_size_v

def printNodes():
    for i in nodes:
        print(i)

def calculateDistances(fin): #todos hacia fin
    if not nodes[fin].active:
        print("Error. nodo destino no existente.")
        return []
    distances = [inf for _ in range(num_nodes)]
    for i in range(0,num_nodes):
        if nodes[i].active:
            distances[i] = distance.euclidean(nodes[i].pos,nodes[fin].pos)
        else:
            distances[i] = inf
    return distances
	
def deleteRange(ini,fin):
	for i in range(int(ini),int(fin)+1):
		nodes[i].deactivate()

mAdy = matAdy()#matriz adyacencia  
nodes = generateNodes() #lista 1-dimensional de nodos
#deleteRange(4,6)  #borrar nodos del 0 al 4
generateEdges()
drawNodes(nodes)
mAdy.drawEdges()
dis = calculateDistances(8)
print("dis: ",dis)

#printNodes()

def best_first():
    global nodo_ini
    global nodo_fin

    dis = calculateDistances(nodo_fin)
    print("dis: ",dis)

    ini = nodo_ini
    fin = nodo_fin
    if(ini > fin):
          temp=ini
          ini=fin
          fin=temp
    v_pq = []
    visited = {}
    path = []
    heapq.heappush(v_pq, (0,ini))

    visited[ini] = None

    while len(v_pq) > 0:
        vertex = heapq.heappop(v_pq)
        path.append (vertex[1])
        if (vertex[1] == fin):
            for node in visited:
                print("n:",node, "d:", dis[node])
                nodes[node].color = [0,153,153]
                coloredNodes.append(node)
                pygame.display.update(nodes[node].circle)
            for i in path:
                nodes[i].color = [0,255,0]
                pygame.display.update(nodes[i].circle)
            return visited
        for i in range(ini,num_nodes):
            if mAdy.mat[vertex[1]][i] == 1 and i not in visited:
                heapq.heappush(v_pq,(dis[i],i))
                visited[i] = ini  
        print(v_pq, path) 
    return None

#-------------------------------------------------
def aStar():
    global nodo_ini
    global nodo_fin

    dis = calculateDistances(nodo_fin)
    print("dis: ",dis)

    ini = nodo_ini
    fin = nodo_fin
    if(ini > fin):
          temp=ini
          ini=fin
          fin=temp
    v_pq = []
    visited = {}
    path = []
    heapq.heappush(v_pq, (0,ini))

    visited[ini] = None

    while len(v_pq) > 0:
        vertex = heapq.heappop(v_pq)
        path.append (vertex[1])
        if (vertex[1] == fin):
            for node in visited:
                print("n:",node, "d:", dis[node])
                nodes[node].color = [0,153,153]
                coloredNodes.append(node)
                pygame.display.update(nodes[node].circle)
            for i in path:
                nodes[i].color = [0,255,0]
                pygame.display.update(nodes[i].circle)
            return visited
        for i in range(ini,num_nodes):
            if mAdy.mat[vertex[1]][i] == 1 and i not in visited:
                heapq.heappush(v_pq,(dis[i]+distance.euclidean(nodes[i].pos,nodes[fin].pos),i))
                visited[i] = ini  
        print(v_pq, path) 
    return None

    
def detectClickOnNode():
    global nodo_ini
    global nodo_switch
    global camino
    mousePos = pygame.mouse.get_pos()
    for i in range(0,len(nodes)):
        if nodes[i].circle is not None:
            if nodes[i].circle.collidepoint(mousePos):
                #pygame.event.get()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if nodo_switch == True:
                        clearNodes()
                        
                        nodes[i].color = [255,255,255]
                        pygame.display.update(nodes[i].circle)
                        coloredNodes.append(i)
                        pygame.time.wait(200)
                        
                        nodo_ini = i
                        nodo_switch = False
                        
                    else:
                        nodes[i].color = [255,255,255]
                        pygame.display.update(nodes[i].circle)
                        coloredNodes.append(i)
                        pygame.time.wait(200)
                        global nodo_fin
                        nodo_fin = i
                        # BFS(nodo_ini,nodo_fin)
                        #print(camino)
                        #camino = []
                        nodo_switch = True

def clearNodes():
    print(coloredNodes)
    for i in coloredNodes:
        if nodes[i] is not None:
            nodes[i].color = [0,0,255]
            pygame.display.update(nodes[i].circle)
    coloredNodes.clear()

Button(1170, 500, 100, 50, "556B2F", "A*",  aStar, True)
Button(1170, 600, 100, 50, "556B2F", "BestFS",  best_first, True)
botones = ((1170, 500, 100, 50),(1170, 600, 100, 50))

font = pygame.font.SysFont("Consolas", 55)
manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 6)
textinput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=font)
textinput.cursor_width = 4
textinput.cursor_blink_interval = 400 # blinking interval in ms
textinput.antialias = False
textinput.font_color = (0, 85, 170)

while 1:
    DISPLAYSURF.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            deleteRange(textinput.value.split("-")[0],textinput.value.split("-")[1])
            mAdy = matAdy()
            generateEdges()
        
    for object in objects:
        object.process()

    mAdy.drawEdges()
    drawNodes(nodes)
    
    textinput.update(events)
    DISPLAYSURF.blit(textinput.surface, (1070, 50))
    detectClickOnNode()
    pygame.display.update()
    fpsClock.tick(fps)
