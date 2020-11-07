import tkinter as tk
import numpy as np
from player import Player
from filler import Filler
from random import sample

### DEĞİŞKEN
grid = [64*i for i in range(10)]
puans = np.zeros((10,10),dtype=np.int)
data = []
### OBJELER
oyuncu = Player(0,0,"red")
oyuncu.makeDecision(100)
oyuncu2 = Player(grid[9],grid[9],"blue")
fils = [Filler(-100,-100,"black")]
for i in range(1,5):
    add = np.ones((10-2*i,10-2*i),dtype=np.int)
    puans[i:10-i,i:10-i] += add

root = tk.Tk(className="GAME")
root.wm_maxsize(640,640)
root.wm_minsize(640,640)

canv = tk.Canvas(bg="white",width = 640, height = 640)
canv.pack()
n,resetsayisi=(0,0)
maxhamle=20

def isStucked(gamer):
    global fils
    if gamer.x + 64 > 640-64 or gamer.x - 64 < 0 or gamer.y - 64 < 0 or gamer.y + 64 > 640 - 64:
        return False
    for i in fils:
        if gamer.x+64==i.x and gamer.y == i.y:
            return False
        if gamer.x-64==i.x and gamer.y == i.y:
            return False
        if gamer.y+64==i.y and gamer.x == i.x:
            return False
        if gamer.y-64==i.y and gamer.x == i.x:
            return False
    return True


def selectPlayer(datas):
    k = [i[1]/len(i[0]) for i in datas]
    o = 0
    for i in k:
        if i == max(k):
            #print(datas[o])
            #print(k)
            return datas[o][0]
        o+=1

def loop():
    global n,fils,maxhamle,resetsayisi,data
    n+=1
    print(maxhamle,n)
    if n >= maxhamle:
        n=0
        if isStucked(oyuncu):
            maxhamle-=5
            #resetsayisi-=1
        else:
            data.append([oyuncu.direction[0:maxhamle],oyuncu.puan])
        reset()
        #oyuncu.direction[:maxhamle] = selectPlayer(data)
        maxhamle+=5
        #print(data)
    if resetsayisi==3:
        resetsayisi=0
        #oyuncu.makeDecision(100)
        oyuncu.direction[:maxhamle-len(fils)] = selectPlayer(data)
        print(maxhamle-len(fils))
        data=[]
    a = oyuncu.move(oyuncu.direction[n],fils)
    if a != False:
        oyuncu.puan += puans[oyuncu.x // 64, oyuncu.y // 64]
        fils.append(a)
    else:
        oyuncu.direction.pop(n)
        n-=1
        maxhamle-=(not isStucked(oyuncu))
        [oyuncu.direction.append(sample([0,1,2,3],1)[0]) for i in range(10)]
    root.after(50,loop)

def draw():
    canv.delete("all")
    [canv.create_line(i,0,i,640) for i in range(0,640,64)]
    [canv.create_line(0,i,640,i) for i in range(0,640,64)]
    #canv.create_rectangle(grid[5],grid[3],grid[5]+64,grid[3]+64,fill="black")
    for i in range(10):
        for j in range(10):
            if puans[i,j] == 0:
                continue
            canv.create_text(grid[i]+32,grid[j]+32,fill="darkblue",font="Times 20 bold",text=str(puans[i,j]))
    oyuncu.draw(canv)
    oyuncu2.draw(canv)
    canv.create_text(oyuncu.x + 32, oyuncu.y + 32, fill="black", text=str(oyuncu.puan), font="Times 20 bold")
    canv.create_text(oyuncu2.x+32,oyuncu2.y+32,fill="black",text=str(oyuncu2.puan),font="Times 20 bold")
    [i.draw(canv) for i in fils]
    root.after(50,draw)

loop()
draw()
a = False
def yon(e):
    global a
    a = False
    #print(e.char)
    if e.char=="w":
        a = oyuncu.move(0,fils)
    if e.char=="s":
        a = oyuncu.move(1,fils)
    if e.char=="d":
        a = oyuncu.move(2,fils)
    if e.char=="a":
        a = oyuncu.move(3,fils)
    if a != False:
        oyuncu.puan += puans[oyuncu.x // 64, oyuncu.y // 64]
        fils.append(a)
root.bind("<w>",yon)
root.bind("<a>",yon)
root.bind("<s>",yon)
root.bind("<d>",yon)

def yon2(e):
    global a
    a = False
    #print(e.keysym)
    if e.keysym=="Up":
        a = oyuncu2.move(0,fils)
    if e.keysym=="Down":
        a = oyuncu2.move(1,fils)
    if e.keysym=="Right":
        a = oyuncu2.move(2,fils)
    if e.keysym=="Left":
        a = oyuncu2.move(3,fils)
    if a != False:
        oyuncu2.puan += puans[oyuncu2.x // 64, oyuncu2.y // 64]
        fils.append(a)
def reset(e=False):
    global oyuncu2,oyuncu,fils,resetsayisi
    resetsayisi+=1
    #oyuncu = Player(0,0,"red")
    oyuncu.x=0
    oyuncu.y=0
    oyuncu.puan=0
    oyuncu2 = Player(grid[9],grid[9],"blue")
    fils = [Filler(-312,-123,color="black")]
root.bind("<Up>",yon2)
root.bind("<Down>",yon2)
root.bind("<Left>",yon2)
root.bind("<Right>",yon2)
root.bind("<o>",reset)
tk.mainloop()