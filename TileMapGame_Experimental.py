import pygame, sys, os
from player import *
from gamemap import *
from gamecontroller import *
pygame.init()

W,H = 480,480
screen = pygame.display.set_mode((W,H))



#SET TILE SIZE - Each tile must be same size for this system.
tileSize = 48

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
bgMap1 = [['GNW', 'GN','GN',  'GN',  'GN',  'GN', 'GN',  'GN',  'GN',  'GNE' ],
          ['GW',  'G' ,'G',   'G',   'G',   'G',  'G',   'G',   'G',   'GE' ],
          ['GW',  'G' ,'GBD', 'GBD', 'D',   'D',  'G',   'G',   'G',   'GE' ],
          ['GW',  'G', 'GBD', 'CW1', 'CW1', 'D',  'G',   'G',   'G',   'GE' ],
          ['GW',  'G', 'GBD', 'CW1', 'CW0', 'D',  'CF4', 'CF2', 'CF4', 'GE' ],
          ['GW',  'G', 'GBD', 'GBD', 'D',   'D',  'CF2', 'CF4', 'CF2', 'GE' ],
          ['GW',  'G', 'GBD', 'GNW', 'D',   'G',  'G',   'G',   'G',   'GE' ],
          ['GW',  'D', 'D',   'GSE', 'GBD', 'GBD','G',   'G',   'G',   'GE' ],
          ['GW',  'G', 'G',   'GBD', 'GBD', 'G',  'G',   'G',   'G',   'GE' ],
          ['GSW', 'GS','GS',  'GS',  'GS',  'GS', 'GS',  'GS',  'DPD', 'GSE' ]]


bgMap2 = [['GNW', 'GN', 'GN',  'GN',  'GN',  'GN', 'GN', 'GN', 'DPU','GNE' ],
          ['GW',  'G' , 'G',   'G',   'G',   'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G' , 'GBD', 'GBD', 'D',   'D',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'CW0', 'CW0', 'D',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'CW0', 'SDR', 'D',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'GBD', 'D',   'D',  'G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'GBD', 'GNW', 'D',   'G',  'G',  'G',  'G',  'GE' ],
          ['GW',  'D',  'D',   'GSE', 'GBD', 'GBD','G',  'G',  'G',  'GE' ],
          ['GW',  'G',  'G',   'GBD', 'GBD', 'G',  'G',  'G',  'G',  'GE' ],
          ['GSW', 'GS', 'GS',  'GS',  'GS',  'GS', 'GS', 'GS', 'GS', 'GSE' ]]

#make game background map as a list of lists. 
bgMap3 = [['CW0', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1',  'CW1',  'CW1',  'CW0' ],
          ['CW1', 'CB1', 'CB1', 'CB3', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3',  'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3',  'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3',  'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CF2',  'CF4',  'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'SUL', 'CB3', 'CB3',  'CF4',  'CF2',  'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'CB3',  'CB3',  'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'D',    'D',    'CW1' ],
          ['CW1', 'CB1', 'CB1', 'CB2', 'CB2', 'CB3', 'CB3',  'D',    'D',    'CW1' ],
          ['CW0', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1', 'CW1',  'CW1',  'CW1',  'CW0' ]]


#Create GameMap object to organize the map and its dictionary in one place
gameMap1 = GameMap(bgMap1,imgDict1, tileSize)
gameMap2 = GameMap(bgMap2,imgDict1, tileSize)
gameMap3 = GameMap(bgMap3,imgDict1, tileSize)
worldMap = [[gameMap1, None],
            [gameMap2, gameMap3]]

#Create the player
playerImg = pygame.image.load("images\\hungry_ghost.png").convert()
playerImg.set_colorkey((0,0,0))
player = Player(playerImg, 8, 1, tileSize)

gc = GameController(worldMap, player)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gc.movePlayer("down")
            elif event.key == pygame.K_UP:
                 gc.movePlayer("up")
            elif event.key == pygame.K_LEFT:
                 gc.movePlayer("left")
            elif event.key == pygame.K_RIGHT:
                 gc.movePlayer("right")
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    gc.update(screen)
    
    clock.tick(60)
    pygame.display.update()
    
