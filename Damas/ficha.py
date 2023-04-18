
class Ficha():
    def __init__(self,jugador,x,y,dir):
        self.jugador = jugador
        self.x = x
        self.y = y
        self.dir =dir

    def __str__(self):
        return str(self.jugador)
    
    def __repr__(self):
        return str(self.jugador)

    def moverD(self,ID):
        if(ID == "D"):

            if(self.dir == "abajo"):
                # 2 0 - 3 1
                if self.x+1 > 7 or self.y+1> 7:
                    return False   
                self.x=self.x+1 #0-3 1-4
                self.y=self.y+1
                return True

            else:
                if self.x-1 < 0 or self.y+1>7:
                    return False
                self.x=self.x-1 #5-2 4-3
                self.y=self.y+1
                return True
        elif(ID == "I"):
            if(self.dir == "abajo"):
                if self.x+1 > 7 or self.y-1<0:
                    return False
                self.x=self.x+1 #0-3 1-4
                self.y=self.y-1
                return True
            else:
                #5 7 - 4 6
                if self.x-1 < 0 or self.y-1<0:
                    return False
                self.x=self.x-1 #0-3 1-4
                self.y=self.y-1
                return True
    
    def mover(self, x, y):
        if (x<0 or x>7 or y<0 or y>7):
            return False
        self.x = x
        self.y = y
        return True
        
    def printPos(self):
        print("pos: ",self.x,self.y)