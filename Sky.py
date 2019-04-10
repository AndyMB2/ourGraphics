#ourGraphics.py by Andy B & Fernando A

from graphics import *

def draw_rect(rX, rY, rW, rH, rCol, rWin):
    sC = Rectangle(Point(rX, rY), Point(rX + rW, rY + rH))
    sC.setFill(rCol)
    sC.draw(rWin)

skyX = 800
skyY = 800

skyWin = GraphWin("SkyScraperScenery", skyX, skyY)
skyWin.setCoords(0, 0, skyX, skyY)

draw_rect(0, 0, skyX, skyY, "sky blue", skyWin) 
draw_rect(250, 0, skyX / 3, 700, "grey", skyWin)
