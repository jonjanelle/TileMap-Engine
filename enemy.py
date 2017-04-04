#Class to describe the attributes and behaviors of game enemies.
#Currently all enemies do the same amount of damage and move at the
#same speed, but differ in their appearances and movement patterns
#
#ASSIGNMENT:
#Currently only the paceHoriz movement method is finished. Enemies
#with actionType "pace_horiz" will move back and forth between the
#left and right edges of the game map in a straight line. When an edge
#or impassable tile is hit, the enemy will turn around and travel in the
#other direction
#
#(1) Carefully analyze the paceHoriz method until you clearly understand
#    how it works.
#
#(2) Complete the paceVert method. This method is similar to paceHoriz,
#    but causes enemies to move vertically in a straight line between
#    the top and bottom of the game map.
#
#(3) Complete the circleCW method
#
#(4) Complete the circleCCW method
#

import pygame, random

class Enemy:
    def __init__(self, img, row, col, tileSize, actionType="pace_horiz"):
        self.img = img
        self.row = row
        self.col = col
        self.tileSize = tileSize
        self.actionType = actionType #pace_horiz, pace_vert circleCW,circleCCW
        self.moveDir = "right" #up, down, left, or right
        self.moveTimer = 1 #leave this for now

    #Enemy will pace in a straight line horizontally. 
    def paceHoriz(self, gameMap):
        if self.moveDir == "right":
            #If enemy won't move out of right bounds or hit impassable
            if self.col+1 < gameMap.nCols and gameMap.getTile(self.row,self.col+1).passable:
                self.col+=1
            else: #about to go out of bounds or an impassable tile hit.
                self.moveDir = "left"

        elif self.moveDir == "left":
            if self.col-1 >= 0 and gameMap.getTile(self.row,self.col-1).passable:
                self.col-=1
            else:
                self.moveDir = "right"

    #Enemy will travel in a straight line vertically
    #between the top and bottom of the GameMap
    def paceVertical(self, gameMap):
        if self.moveDir in ["right","left"]:
            self.moveDir = "down"
            
        if self.moveDir == "down":
            #If enemy won't move out of right bounds or hit impassable
            if self.row+1 < gameMap.nRows and gameMap.getTile(self.row+1,self.col).passable:
                self.row+=1
            else: #about to go out of bounds or an impassable tile hit.
                self.moveDir = "up"

        elif self.moveDir == "up":
            if self.row-1 >= 0 and gameMap.getTile(self.row-1,self.col).passable:
                self.row-=1
            else:
                self.moveDir = "down"

    #Enemy will travel in a clockwise circular path
    #around the outside edge of the level. When an edge
    #or impassible tile is reached, turn right 90 degrees
    #and move forward. 
    def circleCW(self, gameMap):
        if self.moveDir == "right":
            if self.col+1 < gameMap.nCols and gameMap.getTile(self.row,self.col+1).passable:
                self.col+=1
            else:
                self.moveDir = "down"

        elif self.moveDir == "down":
            if self.row+1 < gameMap.nRows and gameMap.getTile(self.row+1,self.col).passable:
                self.row+=1
            else:
                self.moveDir = "left"

        elif self.moveDir == "left":
            if self.col-1 >= 0 and gameMap.getTile(self.row,self.col-1).passable:
                self.col-=1
            else:
                self.moveDir = "up"

        elif self.moveDir == "up":
            if self.row-1 >= 0 and gameMap.getTile(self.row-1,self.col).passable:
                self.row-=1
            else:
                self.moveDir = "right"

    #Enemy will travel in a counter-clockwise circular path
    #around the outside edge of the level. When an edge
    #or impassible tile is reached, turn left 90 degrees
    #and move forward.
    def circleCCW(self, gameMap):
        pass

    #Enemy will always move in a circle around the outer edge of the game
    #map
    def stickToEdges(self, gameMap, player):
        pass

    
    def move(self, gameMap):
        if self.actionType == "pace_horiz":
            self.paceHoriz(gameMap)
        elif self.actionType == "pace_vert":
            self.paceVertical(gameMap)
        elif self.actionType == "circleCW":
            self.circleCW(gameMap)

    
    def update(self,screen, gameMap):
        if self.moveTimer == 1:
            self.move(gameMap)
            self.moveTimer = 1 - self.moveTimer
        else:
            self.moveTimer = 1 - self.moveTimer

        screen.blit(self.img, (self.col*self.tileSize, self.row*self.tileSize))    

