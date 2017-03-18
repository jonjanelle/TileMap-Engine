from gamemap import *

class GameController:
    def __init__(self, worldMap, player):
        self.worldMap = worldMap
        self.player = player
        self.row = 0
        self.col = 0


    def movePlayer(self,direction):
        cMap = self.worldMap[self.row][self.col] #get current map
        
        if direction == 'up':
            if self.player.row > 0:
                if cMap.mapDict[cMap.mapGrid[self.row-1][self.col]].passable == True:   
                    self.player.move(direction)
                    
        elif direction == "down":
            if self.player.row < len(cMap.mapGrid)-1:
                if cMap.mapDict[cMap.mapGrid[self.player.row+1][self.player.col]].passable == True:
                   self.player.move(direction)
        elif direction == "right":
            if self.player.col < len(cMap.mapGrid[0])-1:
                if cMap.mapDict[cMap.mapGrid[self.player.row][self.player.col+1]].passable == True:
                   self.player.move(direction)
        elif direction == "left":
            if self.player.col > 0: 
                if cMap.mapDict[cMap.mapGrid[self.player.row][self.player.col-1]].passable == True:
                   self.player.move(direction)
        self.checkForExit() 
        
    def checkForExit(self):
        cMap = self.worldMap[self.row][self.col]
        currentTile = cMap.mapDict[cMap.mapGrid[self.player.row][self.player.col]]
        if isinstance(currentTile, ExitTile):
            if currentTile.exitDir=="down":
                self.row+=1
                if currentTile.resetPos:
                    self.player.row=0
            elif currentTile.exitDir=="up":
                self.row-=1
                if currentTile.resetPos:
                    self.player.row = len(cMap.mapGrid[0])-1
            elif currentTile.exitDir=="right":
                self.col+=1
                if currentTile.resetPos:
                    self.player.col = 0
            elif currentTile.exitDir=="left":
                self.col-=1
                if currentTile.resetPos:
                    self.player.col = len(cMap.mapGrid)-1
            
            
        
    def update(self,screen):
        self.worldMap[self.row][self.col].update(screen)
        self.player.update(screen)
        
        
