import pygame
class Player:
    def __init__(self, img, row, col, tileSize):
        self.img = img   #The image surface for the player.
        self.row = row   
        self.col = col
        self.tileSize = tileSize
        self.facing = "left"

    def update(self, screen):
        screen.blit(self.img,(self.col*self.tileSize,self.row*self.tileSize))

    #Respond to a move request
    def move(self, direction):
        if direction == 'up':
            self.row -= 1

        elif direction == "down":
            self.row += 1

        elif direction == "right":
            if self.facing == "left":
                self.img = pygame.transform.flip(self.img, True,False)
                self.facing = "right"
            self.col += 1

        elif direction == "left":
            if self.facing == "right":
                self.img = pygame.transform.flip(self.img, True,False)
                self.facing = "left"
            self.col-=1
