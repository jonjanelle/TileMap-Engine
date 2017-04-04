import pygame
from gamemap import *

class GameController:
    def __init__(self, worldMap, player):
        self.worldMap = worldMap
        self.row = 0  #Refer to the current (row, col) position in the worldmap
        self.col = 0  
        self.player = player
        self.viewMsg1 = "What are those?"
        self.viewMsg2 = "I've got to get out of here!"
        self.inventoryOpen = False

    #check whether the player is currently standing on an item. If yes,
    #then add this item to the player's inventory and remove it from the
    #current map
    def pickupItem(self):
        cMap = self.worldMap[self.row][self.col] #get current map
        items = cMap.items #get items list of current map
        for i in items:
            if i.row == self.player.row and i.col == self.player.col:
                self.viewMsg1 = "You grabbed: "+i.name
                self.viewMsg2 = i.description
                self.player.inventory.append(i)
                cMap.items.remove(i)

        
    # Check whether player can move in the requested direction
    # direction can be 'up','down','left', or 'right'
    def checkInput(self):
        cMap = self.worldMap[self.row][self.col] #get current map
        keys = pygame.key.get_pressed()        

        if keys[pygame.K_i]:
            self.inventoryOpen = True

        elif keys[pygame.K_g]:
            self.pickupItem()
        
        elif keys[pygame.K_UP]:
            if self.player.row > 0:
                if cMap.mapDict[cMap.mapGrid[self.player.row-1][self.player.col]].passable == True:   
                    self.player.move("up")
                    
        elif keys[pygame.K_DOWN]:
            if self.player.row < len(cMap.mapGrid)-1:
                if cMap.mapDict[cMap.mapGrid[self.player.row+1][self.player.col]].passable == True:
                   self.player.move("down")

        elif keys[pygame.K_RIGHT]:
            if self.player.col < len(cMap.mapGrid[0])-1:
                if cMap.mapDict[cMap.mapGrid[self.player.row][self.player.col+1]].passable == True:
                   self.player.move("right")

        elif keys[pygame.K_LEFT]:
            if self.player.col > 0: 
                if cMap.mapDict[cMap.mapGrid[self.player.row][self.player.col-1]].passable == True:
                   self.player.move("left")
                   
        self.checkForExit() 


    # Check whether the player is current standing on an ExitTile
    # If so, update the position in the worldMap
    def checkForExit(self):
        cMap = self.worldMap[self.row][self.col]
        pressed = pygame.key.get_pressed()
        currentTile = cMap.mapDict[cMap.mapGrid[self.player.row][self.player.col]]

        if isinstance(currentTile, ExitTile) and pressed[pygame.K_SPACE]:
            if currentTile.exitDir=="down":
                self.row+=1
                if currentTile.resetPos:
                    self.player.row=1

            elif currentTile.exitDir=="up":
                self.row-=1
                if currentTile.resetPos:
                    self.player.row = len(cMap.mapGrid[0])-2

            elif currentTile.exitDir=="right":
                self.col+=1
                if currentTile.resetPos:
                    self.player.col = 1

            elif currentTile.exitDir=="left":
                self.col-=1
                if currentTile.resetPos:
                    self.player.col = len(cMap.mapGrid)-2
                    
            #reset view messages when entering a new region
            self.viewMsg1 = ""
            self.viewMsg2 = ""



    def drawInventory(self, screen):
        W=screen.get_width()
        H=screen.get_height()
        font=pygame.font.SysFont(None, 32)
        vert = 50
        horiz = 20
        viewPortHeight = 100
        tileSize = 32

        #Draw the inventory background box
        pygame.draw.rect(screen, (0,0,0), (0, 0, W, H-viewPortHeight))
        textSurf1 = font.render("Inventory",True,(255,255,255))
        screen.blit(textSurf1,(W/2-textSurf1.get_width()/2, 20))
        ########################

        itemRects = []
        #Draw items in inventory
        for i in range(len(self.player.inventory)):
            if pygame.Rect(horiz, vert, tileSize, tileSize).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (100,100,100),(horiz, vert, tileSize, tileSize))
                itemRects.append(pygame.Rect(horiz, vert, tileSize, tileSize))
                                                                         
            screen.blit(self.player.inventory[i].img,(horiz, vert))
            horiz+=35
            if horiz > W-35:
                vert+=50
                horiz=20
                
        #update the display            
        pygame.display.update()
        return itemRects

        
    #Display the player's inventory screen
    def showInventory(self,screen):
        itemRects = self.drawInventory(screen)

        #wait for user to close inventory
        while (self.inventoryOpen):
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_i:
                        self.inventoryOpen=False

            mousePos = pygame.mouse.get_pos()
            found = False
            for i in range(len(itemRects)):
                if itemRects[i].collidepoint(mousePos):
                    found = True
                    self.drawInventory(screen)
                    pygame.draw.rect(screen, (100,100,100), itemRects[i])
                    screen.blit(self.player.inventory[i].img, (itemRects[i].x, itemRects[i].y))
                    self.viewMsg1 = "Item Name: " + self.player.inventory[i].name
                    self.viewMsg2 = self.player.inventory[i].description

            if found == False:
                self.drawInventory(screen)
                    

    # Update by drawing current map in worldMap, player, and
    # enemies to screen surface
    def update(self,screen):
        if (self.inventoryOpen):
            self.showInventory(screen)
        else:
            self.checkInput()
            self.worldMap[self.row][self.col].update(screen)
            self.player.update(screen)
        
