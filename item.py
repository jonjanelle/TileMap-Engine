class Item:
    def __init__(self, img, row, col, name, description, tileSize):
        self.img=img
        self.row = row
        self.col = col
        self.name=name
        self.description=description
        self.tileSize = tileSize

    def update(self, screen):
        screen.blit(self.img, (self.col*self.tileSize, self.row*self.tileSize))
