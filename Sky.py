#ourGraphics.py by Andy B & Fernando A
from random import randint
from graphics import *

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

bgR=Rectangle(Point( 0,0 ), Point(skySz, skySz))
bgR.setFill("skyblue")
bgR.draw(skyWin)

for i in range (6):
    draw_cloud(skySz, 600, 750, 20, "white")
