from random import sample
from filler import Filler

class Player:
    def __init__(self,x,y,color="black"):
        self.x = x
        self.puan = 0
        self.y = y
        self.color = color
        self.direction=[]
    def draw(self, canva):
        canva.create_rectangle(self.x,self.y,self.x+64,self.y+64,fill=self.color)
    def makeDecision(self,n):
        self.direction = [sample([0,1,2,3],1)[0] for i in range(n)]

    def move(self,yon,fils):
        fil = Filler(self.x,self.y,self.color)
        if yon == 0 and self.y-64>=0:#W up
            for i in fils:
                if i.y == self.y-64 and self.x == i.x:
                    return False
            self.y-=64
        if yon == 1 and self.y+64<=640-64:#S down
            for i in fils:
                if i.y == self.y+64 and self.x == i.x:
                    return False
            self.y+=64
        if yon == 2 and self.x+64<=640-64:#D right
            for i in fils:
                if i.x == self.x+64 and self.y == i.y:
                    return False
            self.x+=64
        if yon == 3 and self.x-64>=0:#A left
            for i in fils:
                if i.x == self.x-64 and self.y == i.y:
                    return False
            self.x-=64
        if fil.x == self.x and fil.y == self.y:
            return False
        return fil