from tkinter import *
from matrix import matrix
import threading
from numpy import random
global duzina
duzina = 8
smer = "r"
global nahr
nahr = False
global stara_x
global stara_y
stara_x=0
stara_y=0
Snake = Tk()
my_canvas = Canvas(Snake, width=len(matrix[0])*20,height=len(matrix)*20,background="black")
my_canvas.grid(row=0,column=0)
Snake.title( "Snake_Py by LuBu" )
def createAnApple():
    apple_x = random.randint(len(matrix[0])-2)+1
    apple_y = random.randint(len(matrix)-2)+1
    my_canvas.create_rectangle(apple_x*20,apple_y*20,apple_x*20+20,apple_y*20+20, fill="green")
    matrix[apple_y][apple_x] = -3

def leftClick(event):
    global smer
    if(not(smer == "r")):
        smer = "l"
def rightClick(event):
    global smer
    if(not(smer == "l")):
        smer = "r"
def upClick(event):
    global smer
    if(not(smer=="d")):
        smer = "u"
def downClick(event):
    global smer
    if(not(smer == "u")):
        smer = "d"
def provera(x,y):
    if(matrix[y][x] > 0 or matrix[y][x] == -2):
        interval.cancel()
        return False
    elif(matrix[y][x] == -3):
        global duzina
        global nahr
        nahr = True
        duzina+=1
        return True
    else:
        return True
def wallDraw():
    for i in range(len(matrix)):
        if((i == 0) or (i == len(matrix)-1)):
            for k in range(len(matrix[0])):
                my_canvas.create_rectangle(k*20,i*20,k*20+20,i*20+20, fill="red")
        else:
            my_canvas.create_rectangle(0,i*20,20,i*20+20, fill="red")
            my_canvas.create_rectangle((len(matrix[0])-1)*20,i*20,len(matrix[0])*20,i*20+20, fill="red")
    createAnApple()
       
def draw_things():
    for i in range(1,duzina+1):
        poz_y = [f for f in range(len(matrix)) if i in matrix[f]][0]
        poz_x = matrix[poz_y].index(i)
        my_canvas.create_rectangle(poz_x*20,poz_y*20,poz_x*20+20,poz_y*20+20, fill="white")

def moveInMatrix():
    global nahr
    global interval
    interval = threading.Timer(0.8-(duzina/100), moveInMatrix)
    interval.start()
    for i in range(1,duzina+1):
        if(i == 1):
            poz_y = [f for f in range(len(matrix)) if 1 in matrix[f]][0]
            poz_x = matrix[poz_y].index(1)
            matrix[poz_y][poz_x] = 1001
            if(smer == "r" and provera(poz_x+1,poz_y)):
                matrix[poz_y][poz_x+1] = 1
            elif(smer == "u" and provera(poz_x,poz_y-1)):
                matrix[poz_y-1][poz_x] = 1
            elif(smer == "l" and provera(poz_x-1,poz_y)):
                matrix[poz_y][poz_x-1] = 1
            elif(smer == "d" and provera(poz_x,poz_y+1)):
                matrix[poz_y+1][poz_x] = 1
            else:
                break
        else:
            stara_y = [f for f in range(len(matrix)) if i in matrix[f]][0]
            stara_x = matrix[stara_y].index(i)
            poz_y = [f for f in range(len(matrix)) if 1001 in matrix[f]][0]
            poz_x = matrix[poz_y].index(1001)
            matrix[poz_y][poz_x] = i
            matrix[stara_y][stara_x] = 1001
    try:
        if(nahr == False):
            matrix[stara_y][stara_x] = 0
            my_canvas.create_rectangle(stara_x*20,stara_y*20,stara_x*20+20,stara_y*20+20, fill="black")
            draw_things()
        else:
            poz_y = [f for f in range(len(matrix)) if 1 in matrix[f]][0]
            poz_x = matrix[poz_y].index(1)
            my_canvas.create_rectangle(poz_x*20,poz_y*20,poz_x*20+20,poz_y*20+20, fill="white")
            matrix[stara_y][stara_x] = duzina
            nahr = False
            createAnApple()
    except:
        print("You died")
    
wallDraw()
draw_things()

moveInMatrix()
my_canvas.bind("<Left>", leftClick)
my_canvas.bind("<Right>", rightClick)
my_canvas.bind("<Up>", upClick)
my_canvas.bind("<Down>", downClick)
my_canvas.focus_set()
my_canvas.pack()
Snake.mainloop()
