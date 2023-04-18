
def stringmatrix(pref, matrix):
    m = pref
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            m += str(matrix[i][j]) + " "
        m += "\n" + pref
    return m

class Nodo:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.level = None

class node():
    def __init__(self, data = None, children = []):
        self.data = data
        self.children = children

    def printnode(self, level=0):
        print(stringmatrix('\t'*level, self.data))
        for child in self.children:
            child.printnode(level + 1)
    
    def insert(self, data):
        
        self.children.append(node(data))
        self.children[-1].children = []
        #print(self.data, len(self.children))
        return self.children[-1]
    
class Arbol:
    def __init__(self):
        self.root = None

    def _insert(self, data):
        if not self.root:
            self.root = node(data)
            return
        self._insert(self.root, data)

    def bfs_tree(self, nodo, data):
        if nodo.data == data:
            return nodo
        for child in nodo.children:
            n = self.bfs_tree(child, data)
            if n != None:
                return n
        return None
        

    # def insert(self, nodo, data):
    #     if not self.root:
    #         self.root = node(data)
    #         return
    #     n = self.bfs_tree(self.root, nodo)
    #     if n:
    #         n.children.append(node(data))

    def insert(self, nodo, data):
        nodo.children.append(node(data))

    # def _insert(self, node, data, level):
    #     if not node:
    #         return Nodo(data)
    #     if data < node.data:
    #         node.left = self._insert(node.left, data, level+1)
    #     else:
    #         node.right = self._insert(node.right, data, level+1)
    #     node.level = level
    #     return node

    # def insert(self, data):
    #     if not self.root:
    #         self.root = Nodo(data)
    #         self.root.level = 0
    #         return
    #     self._insert(self.root, data, 1)

 
    # def print_tree(self):
    #     print("Imprimiendo arbol")
    #     current_level = self.root.level
    #     nodes = [self.root]
    #     while nodes:
    #         current_node = nodes.pop(0)
    #         if current_node.level != None and current_node.level > current_level:
    #             print("\n")
    #             current_level += 1
    #         print(current_node.data, end=' ')
    #         if current_node.left:
    #             nodes.append(current_node.left)
    #         if current_node.right:
    #             nodes.append(current_node.right)
    #     print("Fin de arbol")

    def printTree(self):
        str(self.root)
        print(self.root)