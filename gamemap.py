# A tile has an image, a size, may be occupied by player/enemy,
class Tile:
    def __init__(self, img, tileSize, passable = True):
        self.img = img
        self.tileSize = tileSize
        self.passable = passable #whether game entity can walk on this tile or not.
    
    def update(self, screen, x, y):    
        screen.blit(self.img,(x,y))

class ExitTile(Tile): 
    def __init__(self,img,tileSize,exitDir,resetPos=True):
        Tile.__init__(self,img,tileSize)
        self.exitDir = exitDir
        self.resetPos = resetPos


                 
# A GameMap object containts a 2D array of strings representing Tiles
# and a dictionary associating each string with a Tile object.
class GameMap:
    def __init__(self, mapGrid, mapDict,tileSize):
        self.mapGrid = mapGrid
        self.mapDict = mapDict
        self.tileSize = tileSize
        self.nCols = len(mapGrid[0])
        self.nRows = len(mapGrid)

    #draw all tiles to the screen
    def update(self, screen):
        for i in range(self.nRows):
            for j in range(self.nCols):
                tile = self.mapDict[self.mapGrid[i][j]]
                tile.update(screen,self.tileSize*j, self.tileSize*i)
