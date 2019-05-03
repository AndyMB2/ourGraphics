
 #ourGraphics.py by Andy B & Fernando A
from random import randint
from graphics import *

def draw_rect(rX, rY, rW, rH, rCol, rWin):
    sC = Rectangle(Point(rX, rY), Point(rX + rW, rY + rH))
    sC.setFill(rCol)
    sC.draw(rWin)

def draw_circle(cX, cY, radius, cColor):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(cColor)
    circle.setOutline(cColor)
    circle.draw(skyWin)

def draw_cloud(maxX, minY, maxY, clRad, clColor):
    clX = randint(0, maxX)
    clY = randint(minY, maxY)
    for i in range (10):
        draw_circle(clX + randint(-50, 50), clY+ randint(-20, 20) , clRad , clColor)

skySz = 800

skyWin = GraphWin("SkyScraperScenery", skySz, skySz)
skyWin.setCoords(0, 0, skySz, skySz)

draw_rect(0, 0, skySz, skySz, "sky blue", skyWin) #Background

gX = 258
gH = 3.2
gW = 7
gCol = "white" 

draw_rect(250, 0, skySz / 3, 700, "grey", skyWin)#Tower
draw_rect(gX, 550, skySz / gH, skySz / gW, gCol, skyWin)#window
draw_rect(gX, 420, skySz/ gH, skySz/ gW, gCol, skyWin)
draw_rect(gX, 290, skySz/ gH, skySz/ gW, gCol, skyWin)
draw_rect(gX, 160, skySz/ gH, skySz/ gW, gCol, skyWin)
draw_rect(315, 0, skySz/ 6, skySz/ 5.3, "dark grey", skyWin)#door 
draw_rect(410, 50, skySz/ 40, skySz/ 40, "black", skyWin)#door_nob

bgR=Rectangle(Point( 0,0 ), Point(skySz, skySz))
bgR.setFill("skyblue")
bgR.draw(skyWin)

for i in range (6):
    draw_cloud(skySz, 600, 750, 20, "white")
