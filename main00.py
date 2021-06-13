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

class Character(object):
    def __init__(self):
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

    def loadImage(self, file, name, width, height):
        image = pygame.image.load(os.path.join(file, name))
        imageScaled = pygame.transform.scale(image, (width, height))
        return imageScaled

class Player(Character):
    def __init__(self):
        self.playerPosX = 37.5
        self.playerPosY = 0
        self.knightPosX = 37.5
        self.stagePosX = 0
        self.knight_width = 75
        self.knight_height = 67

        Character.__init__(self)

class Enemy(Character):
    def __init__(self):
        self.at500 = False
        self.enemy_width = 100
        self.enemy_height = 100

        Character.__init__(self)

#print statements for testing
player = Player()
print("player")
print(player.walkCount)
print(player.playerPosX)
print("------------------------------")
enemy = Enemy()
print("enemy")
print(enemy.walkCount)
print(enemy.at500)

player.playerPosX += 100
print(player.playerPosX)

#loadimages
player.loadImage('Assets', 'Default_Character_Block1.png', 100, 100)

#Rectangles defined
knightRect = pygame.Rect(player.knightPosX, 0, player.knight_width, player.knight_height)
knight = pygame.Rect(WIDTH/2 - player.knight_width, 0, player.knight_width, player.knight_height)

enemyKnight = pygame.Rect(WIDTH/2 - enemy.enemy_width, HEIGHT-FLOOR.height-enemy.enemy_height, enemy.enemy_width, enemy.enemy_height)
enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)
