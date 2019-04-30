#ourGraphics.py by Andy B & Fernando A
from random import randint
from graphics import *

def draw_circle(cX, cY, radius, cColor):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(cColor)
    circle.setOutline(cColor)
    circle.draw(skyWin)

def draw_cloud(maxX, minY, maxY, clRad, clColor): 
    draw_circle(randint(0, maxX), randint(minY, maxY),clRad , clColor)

##    draw_circle(skySz,skySz-50, 20, "white")
##    draw_circle(skySz,skySz-50, 20, "white")
##    draw_circle(skySz/2,skySz-50, 20, "white")
##    draw_circle(skySz/2,skySz-50, 20, "white")               

skySz = 800

skyWin = GraphWin("SkyScraperScenery", skySz, skySz)
skyWin.setCoords(0, 0, skySz, skySz)

bgR=Rectangle(Point( 0,0 ), Point(skySz, skySz))
bgR.setFill("skyblue")
bgR.draw(skyWin)


draw_cloud(skySz, 600, 800, 20, "white")
