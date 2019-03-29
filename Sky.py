#ourGraphics.py by Andy B & Fernando A

from graphics import *

skyX = 800
skyY = 800

skyWin = GraphWin("SkyScraperScenery", skyX, skyY)
skyWin.setCoords(0, 0, skyX, skyY)

bgR=Rectangle(Point( 0,0 ), Point(skyX, skyY))
bgR.setFill("skyblue")
bgR.draw(skyWin) 
