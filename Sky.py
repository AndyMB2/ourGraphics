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

draw_rect(0, 0, skyX, skyY, "sky blue", skyWin) #Background

#<<<<<<< HEAD
gX = 258
gH = 3.2
gW = 7
gCol = "white" 

draw_rect(250, 0, skyX / 3, 700, "grey", skyWin)#Tower
draw_rect(gX, 550, skyX / gH, skyY / gW, gCol, skyWin)#window
draw_rect(gX, 420, skyX/ gH, skyY/ gW, gCol, skyWin)
draw_rect(gX, 290, skyX/ gH, skyY/ gW, gCol, skyWin)
draw_rect(gX, 160, skyX/ gH, skyY/ gW, gCol, skyWin)
draw_rect(315, 0, skyX/ 6, skyY/ 5.3, "dark grey", skyWin)#door 
draw_rect(410, 50, skyX/ 40, skyY/ 40, "black", skyWin)#door_nob
