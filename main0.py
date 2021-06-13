import pygame
import os
import time

#HW: make same thing as we did for player, for the enemy, make method for enemyRange and other function, (loading images, animations), work on jump
#HW do image load, try to fix it, maybe make new animation if you can't do anything else
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 5

class character():
   def __init__(self, walkCount, swingCount, swingTrigger, blockTrigger, swinging, blocking, jumping, left, right, still, health, alive, jumpCount):
        self.walkCount = 0
        self.swingCount = 0
        self.swingTrigger = False
        self.blockTrigger = False
        self.swinging = False
        self.blocking = False
        self.jumping = False
        self.left = False
        self.right = True
        self.still = True
        self.health = 100
        self.alive = True
        self.jumpCount = 10

class player(character):
    def __init__(self, playerPosX, playerPosY, knightPosX, stagePosX, knight_width, knight_height, **kw):
        #character.__init__(self, walkCount, swingCount, swingTrigger, blockTrigger, swinging, blocking, jumping, left, right, still, health, alive, jumpCount)
        #super(player, self).__init__(self, walkCount, swingCount, swingTrigger, blockTrigger, swinging, blocking, jumping, left, right, still, health, alive, jumpCount)
        #self.knightRect = knightRect
        #might have to add method for knightrect
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.knightPosX = knightPosX
        self.stagePosX = stagePosX
        self.knight_width = knight_width
        self.knight_height = knight_height

    def def_knightRect(self):
        self.knightRect = pygame.Rect(self.knightPosX, 0, self.knight_width, self.knight_height)

    def def_knight(self):
        self.knight = pygame.Rect(WIDTH/2 - self.knight_width, 0, self.knight_width, self.knight_height)

    def loadImage(self, file, name, width, height):
        image = pygame.image.load(os.path.join(file, name))
        imageScaled = pygame.transform.scale(image, (width, height))
        return imageScaled

# player1 = player()
# player1.def_knightRect()
#
# player.loadImage()
#
# player2 = player()
# player2.def_knight()

class enemy(character):
    def __init__(self, at500, enemy_width, enemy_height):
        self.at500 = at500
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height

    def def_enemyRange(self):
        self.enemyRange = pygame.Rect(self.enemyKnight.x, self.enemyKnight.y, 500, 200)
        #self.enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)
        #might have to add method for enemyRange

    def def_enemyKnight(self):
        self.enemyKnight = pygame.Rect(WIDTH/2 - self.enemy_width, HEIGHT-FLOOR.height-self.enemy_height, self.enemy_width, self.enemy_height)

    def loadImage(self, file, name, width, height):
        image = pygame.image.load(os.path.join(file, name))
        imageScaled = pygame.transform.scale(image, (width, height))
        return imageScaled

testCharacter = character(0, 0, False, False, False, False, False, False, True, True, 100, True, 10)
testEnemy = enemy(False, 100, 100)
testPlayer = player(37.5, 0, 37.5, 0, 75, 67)

# enemy1 = enemy()
# enemy1.def_enemyKnight()
#
# enemy.loadImage('Assets', 'enemy.png', 100, 100)
#
# enemy2 = enemy()
# enemy2.def_enemyRange()

playerplayer = player(playerPosX, playerPosY, knightPosX, stagePosX, knight_width, knight_height)

if playerplayer.swinging:
    print("swinging")
