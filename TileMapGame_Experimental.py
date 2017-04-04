import pygame, sys, os
from player import *
from gamemap import *
from gamecontroller import *
from enemy import *
from item import *

pygame.init()
pygame.font.init()

W,H = 352,420
screen = pygame.display.set_mode((W,H))

#SET TILE SIZE - Each tile must be same size for this system.
tileSize = 32

#Dictionary associates string codes with Tile objects.
imgDict1 = {'D':Tile(pygame.image.load("images\\grass_full.png").convert(),tileSize),
            'G':Tile(pygame.image.load("images\\grass0.png").convert(),tileSize),
           'GN':Tile(pygame.image.load("images\\grass_n.png").convert(),tileSize),
           'GS':Tile(pygame.image.load("images\\grass_s.png").convert(),tileSize),
           'GE':Tile(pygame.image.load("images\\grass_e.png").convert(),tileSize),
           'GW':Tile(pygame.image.load("images\\grass_w.png").convert(),tileSize),
           'GNE':Tile(pygame.image.load("images\\grass_ne.png").convert(),tileSize),
           'GSE':Tile(pygame.image.load("images\\grass_se.png").convert(),tileSize),
           'GSW':Tile(pygame.image.load("images\\grass_sw.png").convert(),tileSize),
           'GNW':Tile(pygame.image.load("images\\grass_nw.png").convert(),tileSize),
           'GBD':Tile(pygame.image.load("images\\grass_flowers_blue1.png").convert(),tileSize),
           'CW0':Tile(pygame.image.load("images\\crystal_wall0.png").convert(),tileSize,False),
           'CW1':Tile(pygame.image.load("images\\crystal_wall1.png").convert(),tileSize,False),
           'CF2':Tile(pygame.image.load("images\\crystal_floor2.png").convert(),tileSize),
           'CF4':Tile(pygame.image.load("images\\crystal_floor4.png").convert(),tileSize),
           'CB1':Tile(pygame.image.load("images\\cobble_blood1.png").convert(),tileSize),
           'CB2':Tile(pygame.image.load("images\\cobble_blood2.png").convert(),tileSize),
           'CB3':Tile(pygame.image.load("images\\cobble_blood3.png").convert(),tileSize),
           'DPD':ExitTile(pygame.image.load("images\\dngn_portal.png").convert(),tileSize,"down"),
           'DPU':ExitTile(pygame.image.load("images\\dngn_portal.png").convert(),tileSize,"up"),
           'SDR':ExitTile(pygame.image.load("images\\stone_stairs_down.png").convert(),tileSize,"right",False),
           'SUL':ExitTile(pygame.image.load("images\\stone_stairs_down.png").convert(),tileSize,"left",False)
        }

#Resize all of the Tile images to tileSize
for key in imgDict1.keys():
    imgDict1[key].img = pygame.transform.scale(imgDict1[key].img,(tileSize,tileSize))

#make game background map as a list of lists. 
bgMap1 = [['GNW', 'GN','GN',  'GN',  'GN',  'GN', 'GN',  'GN',  'GN',  'GN', 'GNE' ],
          ['GW',  'G' ,'G',   'G',   'G',   'G',  'G',   'G',   'G',   'G',  'GE' ],
          ['GW',  'G' ,'GBD', 'GBD', 'D',   'D',  'G',   'G',   'G',   'G',  'GE' ],
          ['GW',  'G', 'GBD', 'CW1', 'CW1', 'D',  'G',   'G',   'G',   'G',  'GE' ],
          ['GW',  'G', 'GBD', 'CW1', 'CW0', 'D',  'CF4', 'CF2', 'CF4', 'G',  'GE' ],
          ['GW',  'G', 'GBD', 'GBD', 'D',   'D',  'CF2', 'CF4', 'CF2', 'G',  'GE' ],
          ['GW',  'G', 'GBD', 'GNW', 'GSE',   'G',  'G',   'G',   'G',   'G',  'GE' ],
          ['GW',  'D', 'D',   'GSE', 'GBD', 'GBD','G',   'G',   'G',   'G',  'GE' ],
          ['GW',  'G', 'G',   'GBD', 'GBD', 'G',  'G',   'G',   'G',   'G',  'GE' ],
          ['GSW', 'GS','GS',  'GS',  'GS',  'GS', 'GS',  'GS',  'DPD', 'GS', 'GSE' ]]

bgMap2 = [['GNW', 'GN', 'GN',  'GN',  'GN',  'GN', 'GN', 'GN', 'DPU','GN', 'GNE' ],
          ['GW',  'G' , 'G',   'G',   'G',   'G',  'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G' , 'GBD', 'GBD', 'D',   'D',  'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'CW0', 'CW0', 'D',  'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'CW0', 'SDR', 'D',  'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'GBD', 'D',   'D',  'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'GNW', 'D',   'G',  'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'D',  'D',   'GSE', 'GBD', 'GBD','G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'G',   'GBD', 'GBD', 'G',  'G',  'G',  'G',  'G',  'GE' ],
          ['GSW', 'GS', 'GS',  'GS',  'GS',  'GS', 'GS', 'GS', 'GS', 'GS', 'GSE' ]]

#make game background map as a list of lists. 
bgMap3 = [['CW0', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1',  'CW1',  'CW1', 'CW1', 'CW0' ],
          ['CW1', 'CB1', 'CB1', 'CB3', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3', 'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3', 'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3', 'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CF2',  'CF4', 'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'SUL', 'CB3', 'CB3',  'CF4',  'CF2', 'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3', 'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'D',    'D',   'CB3', 'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'D',    'D',   'CB3', 'CW1' ],
          ['CW0', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1',  'CW1',  'CW1', 'CW1', 'CW0' ]]

#Create some items
iImg1 = pygame.image.load("images\\glittering.png").convert()
iImg1.set_colorkey((0,0,0))
iImg2 = pygame.image.load("images\\book_of_the_dead.png").convert()
iImg2.set_colorkey((0,0,0))
iImg3 = pygame.image.load("images\\staff08.png").convert()
iImg3.set_colorkey((0,0,0))
iImg4 = pygame.image.load("images\\silver_dragon_scales.png").convert()
iImg4.set_colorkey((0,0,0))
iImg5 = pygame.image.load("images\\scroll.png").convert()
iImg5.set_colorkey((0,0,0))

#make item list for map 1
i1 = []
for i in range(16):
    i1.append(Item(iImg1,5+i%4,1+i%5,"Shimmering Tome","The pages spark and glow",tileSize))
#make item list for map 3
i3 = [Item(iImg2,3,1,"Death's Opus","You feel like this book is watching you",tileSize),
      Item(iImg3,8,4,"Staff of Steve","The name 'Steve' is carved into the wood",tileSize),
      Item(iImg4,6,2,"Dragon Scales","You hope the owner of these scales isn't near",tileSize)]


#Create the player
playerImg = pygame.image.load("images\\hungry_ghost.png").convert()
playerImg.set_colorkey((0,0,0))
player = Player(playerImg, 8, 1, tileSize)

#Load images for enemies
eImg1 = pygame.image.load("images\\acid_blob.png").convert()
eImg1.set_colorkey((0,0,0))
eImg2 = pygame.image.load("images\\kobold.png").convert()
eImg2.set_colorkey((255,255,255))
eImg3 = pygame.image.load("images\\deep_troll.png").convert()
eImg3.set_colorkey((0,0,0))
eImg4 = pygame.image.load("images\\deep_elf_sorcerer.png").convert()
eImg4.set_colorkey((0,0,0))
eImg5 = pygame.image.load("images\\flying_skull.png").convert()
eImg5.set_colorkey((0,0,0))

#Create Enemy objects, put enemies in a list
e1 = [Enemy(eImg1, 2, 2, tileSize,"circleCW"),
      Enemy(eImg2, 4, 0, tileSize,"pace_horiz"),
      Enemy(eImg3, 5, 5, tileSize,"pace_vert")]

#Create GameMap object to organize the map and its dictionary in one place
gameMap1 = GameMap(bgMap1,imgDict1, tileSize, e1,i1)
gameMap2 = GameMap(bgMap2,imgDict1, tileSize)
gameMap3 = GameMap(bgMap3,imgDict1, tileSize,[],i3)

#Setup the world map (a collection of GameMaps)
worldMap = [[gameMap1, None],
            [gameMap2, gameMap3]]

#Create the game controller
gc = GameController(worldMap, player)

font=pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    #Update the main game view
    gc.update(screen)
    

    
    clock.tick(12)
    pygame.display.update()
    
