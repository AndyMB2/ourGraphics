#ourGraphics.py by Andy B & Fernando A
from random import randint
from graphics import *

def draw_circle(cX, cY, radius, cColor1, cColor2):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(cColor1)
    circle.setOutline(cColor2)
    circle.draw(skyWin)
                
skySz = 800

skyWin = GraphWin("SkyScraperScenery", skySz, skySz)
skyWin.setCoords(0, 0, skySz, skySz)

bgR=Rectangle(Point( 0,0 ), Point(skySz, skySz))
bgR.setFill("skyblue")
bgR.draw(skyWin)  

draw_circle(skySz/2,skySz-50, 20, "white", "white")

