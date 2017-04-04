# A tile has an image, a size, may be occupied by player/enemy,
class Tile:
    def __init__(self, img, tileSize, passable = True):
        self.img = img
        self.tileSize = tileSize
        self.passable = passable #whether game entity can walk on this tile or not.
    
    def update(self, screen, x, y):    
        screen.blit(self.img,(x,y))

#An ExitTile is a special type of Tile that marks an exit
#to a different region of the game world
class ExitTile(Tile): 
    def __init__(self,img,tileSize,exitDir,resetPos=True):
        '''
        img: The image surface for the tile
        tileSize: The size of the tile
        exitDir: The direction in the worldMap that the tile connects
                 Values are: "up", "down", "left", or "right"
        resetPos: Whether this exit should reset the player's position or
                  if the row/col of the player on the new map is the same
                  as the old. 
        '''
        Tile.__init__(self,img,tileSize)
        self.exitDir = exitDir
        self.resetPos = resetPos

                 
# A GameMap object containts a 2D array of strings representing Tiles
# and a dictionary associating each string with a Tile object.
class GameMap:
    def __init__(self, mapGrid, mapDict,tileSize,enemies=[], items=[]):
        self.mapGrid = mapGrid
        self.mapDict = mapDict
        self.tileSize = tileSize
        self.nCols = len(mapGrid[0])
        self.nRows = len(mapGrid)
        self.enemies = enemies
        self.items = items

    def getTile(self, r, c):
        if r >=0 and r < self.nRows and c >= 0 and c < self.nCols:
            return self.mapDict[self.mapGrid[r][c]]
        else:
            return None
    
    #draw all tiles to the screen
    def update(self, screen):
        for i in range(self.nRows):
            for j in range(self.nCols):
                tile = self.mapDict[self.mapGrid[i][j]]
                tile.update(screen,self.tileSize*j, self.tileSize*i)
        #draw enemies
        for e in self.enemies:
            e.update(screen, self)

        for i in self.items:
            i.update(screen)




