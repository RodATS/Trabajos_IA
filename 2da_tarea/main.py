import pygame, sys
from pygame.locals import DOUBLEBUF
from pygame.locals import QUIT
from scipy.spatial import distance

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


node_size = 2
dim = (3,3)  #row,col
num_nodes = dim[0]*dim[1]

class node:
    def __init__(self,name,pos):
        self.name = name
        self.pos = pos
        self.active = True
    def __str__(self):
        return f"{self.name}({self.pos})"
    def drawNode(self, color):
        if self.active:
            pygame.draw.circle(DISPLAYSURF,color,self.pos,node_size)
        
    def deactivate(self):
        self.active = False

class matAdy:
    def __init__(self):
        self.mat = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
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
    def drawEdges(self, color):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i <= j and self.mat[i][j] == 1:
                    pygame.draw.line(
                        DISPLAYSURF,color,nodes[i].pos,nodes[j].pos)
                
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

def drawNodes(nodes, color):
    for i in nodes:
        i.drawNode(color)
    
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
    
mAdy = matAdy()        
nodes = generateNodes()
nodes[4].deactivate()
generateEdges()
drawNodes(nodes,[0,0,255])
mAdy.drawEdges([0,0,255])
dis = calculateDistances(0)
print("dis: ",dis)

#printNodes()

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for object in objects:
		object.process()
	pygame.display.update()
	fpsClock.tick(fps)