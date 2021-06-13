import pygame
import os
import time

#HW: make same thing as we did for player, for the enemy, make method for enemyRange and other function, (loading images, animations), work on jump
#HW do image load
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 5


# V E R S I O N  1
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
    def __init__(self):
        super().__init__(self, walkCount, swingCount, swingTrigger, blockTrigger, swinging, blocking, jumping, left, right, still, health, alive, jumpCount)

        #self.knightRect = knightRect
        #might have to add method for knightrect
        self.playerPosX = 37.5
        self.playerPosY = 0
        self.knightPosX = 37.5
        self.stagePosX = 0
        self.knight_width = 75
        self.knight_height = 67

    def def_knightRect(self):
        self.knightRect = pygame.Rect(self.knightPosX, 0, self.knight_width, self.knight_height)

    def def_knight(self):
        self.knight = pygame.Rect(WIDTH/2 - self.knight_width, 0, self.knight_width, self.knight_height)

    def loadImage(self, file, name, width, height):
        image = pygame.image.load(os.path.join(file, name))
        imageScaled = pygame.transform.scale(image, (width, height))
        return imageScaled

player1 = player()
player1.def_knightRect()

player.loadImage()

player2 = player()
player2.def_knight()
# player.def_knightRect()
# player.def_knight()


class enemy(character):
    def __init__(self):
        self.at500 = False
        self.enemy_width = 100
        self.enemy_height = 100
        self.enemyKnight = pygame.rect(10, 10, 10, 10)


    def def_enemyKnight(self):
        return pygame.Rect(WIDTH/2 - self.enemy_width, HEIGHT-FLOOR.height-self.enemy_height, self.enemy_width, self.enemy_height)

    def def_enemyRange(self):
        self.enemyRange = pygame.Rect(self.enemyKnight.x, self.enemyKnight.y, 500, 200)
        #self.enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)
        #might have to add method for enemyRange

    def loadImage(self, file, name, width, height):
        image = pygame.image.load(os.path.join(file, name))
        imageScaled = pygame.transform.scale(image, (width, height))
        return imageScaled

enemy1 = enemy()
enemy1.def_enemyKnight()

enemy.loadImage('Assets', 'enemy.png', 100, 100)

enemy2 = enemy()
enemy2.def_enemyRange()


# E N D  O F  V E R S I O N  1

# V E R S I O N  2
#
# class character:
#     def __init__(self, walkCount, swingCount, swingTrigger, blockTrigger, swinging, blocking, jumping, left, right, still, health, alive, jumpCount):
#         self.walkCount = walkCount
#         self.swingCount = swingCount
#         self.swingTrigger = swingTrigger
#         self.blockTrigger = blockTrigger
#         self.swinging = swinging
#         self.blocking = blocking
#         self.jumping = jumping
#         self.left = left
#         self.right = right
#         self.still = still
#         self.health = health
#         self.alive = alive
#         self.jumpCount = jumpCount
#
# testCharacter = character(0, 0, False, False, False, False, False, False, True, True, 100, True, 10)
#
# class player(character):
#     def __init__(self, playerPosX, playerPosY, knightPosX, stagePosX, knight_width, knight_height):
#         super().__init__(self, walkCount, swingCount, swingTrigger, blockTrigger, swinging, blocking, jumping, left, right, still, health, alive, jumpCount)
#         #self.knightRect = knightRect
#         #might have to add method for knightrect
#         self.playerPosX = playerPosX
#         self.playerPosY = playerPosY
#         self.knightPosX = knightPosX
#         self.stagePosX = stagePosX
#         self.knight_width = knight_width
#         self.knight_height = knight_height
#
#     def def_knightRect(self):
#         self.knightRect = pygame.Rect(self.knightPosX, 0, self.knight_width, self.knight_height)
#
#     def def_knight(self):
#         self.knight = pygame.Rect(WIDTH/2 - self.knight_width, 0, self.knight_width, self.knight_height)
#
# player = player(37.5, 0, 37.5, 0, 75, 67)
# player.def_knight()
# player.def_knightRect()
#
# class enemy(character):
#     def __init__(self, at500, enemy_width, enemy_height):
#         self.at500 = at500
#         self.enemy_width = enemy_width
#         self.enemy_height = enemy_height
#
#     def def_enemyRange(self):
#         self.enemyRange = pygame.Rect(self.enemyKnight.x, self.enemyKnight.y, 500, 200)
#         #self.enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)
#         #might have to add method for enemyRange
#
#     def def_enemyKnight(self):
#         self.enemyKnight = pygame.Rect(WIDTH/2 - self.enemy_width, HEIGHT-FLOOR.height-self.enemy_height, self.enemy_width, self.enemy_height)
#
# enemy = enemy(False, 100, 100)
# enemy.def_enemyKnight()
# enemy.def_enemyRange()

# E N D  O F  V E R S I O N  2


#HW - draw flipped blocking and swinging animations, be able to swing while walking


###########################################################################


KNIGHT_WIDTH, KNIGHT_HEIGHT = 75, 67
ENEMY_WIDTH, ENEMY_HEIGHT = 100, 100

knight = pygame.Rect(WIDTH/2 - KNIGHT_WIDTH, 0, KNIGHT_WIDTH, KNIGHT_HEIGHT)
enemyKnight = pygame.Rect(WIDTH/2 - ENEMY_WIDTH, HEIGHT-FLOOR.height-ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT)

KNIGHT1 = pygame.image.load(os.path.join('Assets', 'Default_Character1N.png'))
KNIGHT2 = pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))
KNIGHT3 = pygame.image.load(os.path.join('Assets', 'Default_Character3.png'))
KNIGHT4 = pygame.image.load(os.path.join('Assets', 'Default_Character4.png'))

KNIGHTf1 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png'))
KNIGHTf2 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped2.png'))
KNIGHTf3 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped3.png'))
KNIGHTf4 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped4.png'))

KNIGHTsw1 = pygame.image.load(os.path.join('Assets', 'Default_Character_Swing1.png'))
KNIGHTsw2 = pygame.image.load(os.path.join('Assets', 'Default_Character_Swing2.png'))
KNIGHTsw3 = pygame.image.load(os.path.join('Assets', 'Default_Character_Swing3.png'))

KNIGHTb1 = pygame.image.load(os.path.join('Assets', 'Default_Character_Block1.png'))

KNIGHTs1 = pygame.transform.scale(KNIGHT1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTs2 = pygame.transform.scale(KNIGHT2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTs3 = pygame.transform.scale(KNIGHT3, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTs4 = pygame.transform.scale(KNIGHT4, (KNIGHT_WIDTH, KNIGHT_HEIGHT))

KNIGHTfs1 = pygame.transform.scale(KNIGHTf1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTfs2 = pygame.transform.scale(KNIGHTf2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTfs3 = pygame.transform.scale(KNIGHTf3, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTfs4 = pygame.transform.scale(KNIGHTf4, (KNIGHT_WIDTH, KNIGHT_HEIGHT))

KNIGHTsws1 = pygame.transform.scale(KNIGHTsw1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTsws2 = pygame.transform.scale(KNIGHTsw2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTsws3 = pygame.transform.scale(KNIGHTsw3, (KNIGHT_WIDTH, KNIGHT_HEIGHT))

KNIGHTbs1 = pygame.transform.scale(KNIGHTb1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))

FLOOR1 = pygame.image.load(os.path.join('Assets', 'Floor.png'))
FLOOR1_IMAGE_SCALED = pygame.transform.scale(FLOOR1, (900, 400))

BACKGROUND = pygame.image.load(os.path.join('Assets', 'Background2.png'))
BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
########################################################################

bgWidth, bgHeight = BACKGROUND_IMAGE_SCALED.get_rect().size


flWidth, flHeight = FLOOR1_IMAGE_SCALED.get_rect().size
Character_Movements = [pygame.image.load(os.path.join('Assets', 'Default_Character1N.png')), pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png')), pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))]

stageWidth = bgWidth*2
#player.stagePosX = 0

startScrollingPosX = (WIDTH / 2)

halfW = 37.5
#playerPosY = 500
playerVelocityX = 0

#player.knightrect = pygame.Rect(player.knightPosX, knight.y, KNIGHT_WIDTH, KNIGHT_HEIGHT)

#enemy.enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)

global x
x = 0


walkLeft = [KNIGHTfs1, KNIGHTfs2, KNIGHTfs3, KNIGHTfs4]
walkRight = [KNIGHTs1, KNIGHTs2, KNIGHTs3, KNIGHTs4]
swingRight = [KNIGHTsws1, KNIGHTsws2, KNIGHTsws3]

#class player(object):
    #def __init__(self,x,y,width,height):
        #self.x = kX
        #self.y = kY
        #self.width = kWidth
        #self.height = kHeight
        #self.walkCount = 0

def handle_movement(keys_pressed, knight, playerVelocityX):
    if pygame.key.get_pressed()[pygame.K_a]:
        playerVelocityX = -5
        player.left = True
        player.right = False
        player.still = False

    elif pygame.key.get_pressed()[pygame.K_d]:
        playerVelocityX = 5
        player.left = False
        player.right = True
        player.still = False
        #KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'Default_Character.png'))
    #RIGHT
    else:
        player.still = True
        player.walkCount = 0

    #if not(player.jumping):
        #if pygame.key.get_pressed()[pygame.K_SPACE]:
            #player.jumping = True
            #player.walkCount = 0
            #print("jump")
            #knight.y -= 400
    #else:
        #print("jump2")
        #if player.jumpCount >= -10:
            #neg = 1
            #if player.jumpCount < 0:
                #neg = -1
            #knight.y -= (player.jumpCount ** 2) * 0.5 * neg
            #player.jumpCount -= 1
        #else:
            #player.jumping = False
            #player.jumpCount = 10

    if not(player.jumping):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player.jumping = True
            player.walkCount = 0
    else:
        print("jump2")
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (man.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10
#1234



    player.playerPosX += playerVelocityX

    if player.playerPosX > stageWidth:
         player.playerPosX = stageWidth
         #makes right boundary

    if player.playerPosX < 0:
          player.playerPosX = 0
          #makes left boundary
    if player.playerPosX < startScrollingPosX - knight.width:
          player.knightPosX = player.playerPosX
         # print("here1")
          #if the screen doesn't need to scroll then the knight can move freely
    elif player.playerPosX > stageWidth - startScrollingPosX:
          player.knightPosX = player.playerPosX - stageWidth + WIDTH - knight.width
          #playerPosX = stageWidth + WIDTH
          #print("here12")
          #right boundary
    else:
          #playerPosX = startScrollingPosX - knight.width
          player.knightPosX = startScrollingPosX - knight.width
          player.stagePosX += playerVelocityX

    player.knightrect = pygame.Rect(player.knightPosX, knight.y, KNIGHT_WIDTH, KNIGHT_HEIGHT)
          #print("here123")
          #print(stagePosX)

#rel_x = stagePosX % bgWidth
#WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - bgWidth, 0))
#if rel_x < WIDTH:
       #WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))



        #while x < 200:
            #current_frame += 1
            #knight.y -= 1
            #x += 1


      # RIGHT
      #if keys_pressed[pygame.K_w] and knight.y - vel > 0:
          #knight.y -= vel
      # UP
      #if keys_pressed[pygame.K_s] :
         # knight.y += vel
      # DOWN


def enemyMovement(enemyKnight):
    global knight
    velocity = 2
    rightOfKnight = True
    leftOfKnight = False

    if enemyKnight.x > knight.x:
        rightOfKnight = True
    elif enemyKnight.x < knight.x:
        leftOfKnight = True

    #totalMoved = 0
    #if enemy.x < 500 and at500 == False:
        #enemy.x += velocity
        #totalMoved += velocity
    #elif enemy.x > 50:
        #enemy.x -= velocity
        #at500 = True
    #else:
        #at500 = False



#game loop
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        if knight.y > HEIGHT - FLOOR.height - KNIGHT_HEIGHT:
        #checking if knight is on ground
            player.jumping = False
        if knight.y < HEIGHT - FLOOR.height - KNIGHT_HEIGHT:
        #if knight is on ground dont apply gravity
            knight.y += 5

            #print(HEIGHT - FLOOR.y)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.swinging = True
                    player.swingTrigger = True
                    #swingCount += 1
                    #handle_swing(swingTrigger)
                    #print("swingtrigger", swingTrigger)
                if event.button == 3:
                    player.blocking = True
                    player.blockTrigger = True
                    #handle_block(blockTrigger)
                    #print("blocktrigger", blockTrigger)

            else:
                player.blockTrigger = False

        keys_pressed = pygame.key.get_pressed()
        draw_window()
        handle_movement(keys_pressed, knight, playerVelocityX)
        enemyMovement(enemyKnight)
        handle_damage()

    pygame.quit()

def handle_damage():
    global enemyKnight

    if player.knightrect.colliderect(enemyKnight) and not player.blockTrigger:
        player.health -= 0.1
    if enemyKnight.colliderect(player.knightrect) and player.swingTrigger:
        enemy.health -= 1

    if player.health == 0:
        print("player dead")
        player.alive = False
    if enemy.health == 0:
        enemyKnight.x = 0
        enemyKnight.y = 5000
        enemy.alive = False




#drawing all assets
def draw_window():
    global x

    rel_x = player.stagePosX % BACKGROUND_IMAGE_SCALED.get_rect().width
    WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width,0))
    if rel_x < WIDTH:
         WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))
    x -= 1

    #if player.alive:
        #print("hi")

    #if enemy.alive:
        #WIN.blit(ENEMY_IMAGE_SCALED, (enemyKnight.x, HEIGHT - FLOOR.height - ENEMY_HEIGHT))

    if player.playerPosX > 100000:
        print("test")

    if player.walkCount + 1 >= 30:
        player.walkCount = 0

    if not(player.still):
        if player.left:
            WIN.blit(walkLeft[player.walkCount//10], (player.knightPosX, knight.y))
            player.walkCount += 1
        elif player.right:
            WIN.blit(walkRight[player.walkCount//10], (player.knightPosX, knight.y))
            player.walkCount += 1

    elif player.swingTrigger == True:
        WIN.blit(swingRight[player.swingCount//3], (player.knightPosX, knight.y))
        player.swingCount += 1
        if player.swingCount//3 > 2:
            player.swingCount = 0
            player.swingTrigger = False

    elif player.blockTrigger == True:
        WIN.blit(KNIGHTbs1, (player.knightPosX, knight.y))

        #blockTrigger = False
        #print(blockTrigger, "b")

    elif player.still:
        if player.right:
            WIN.blit(walkRight[0], (player.knightPosX, knight.y))
        elif player.left:
            WIN.blit(walkLeft[0], (player.knightPosX, knight.y))



    if pygame.key.get_pressed()[pygame.K_SPACE] and player.jumping == False:
        pass


    WIN.blit(FLOOR1_IMAGE_SCALED, (rel_x - FLOOR1_IMAGE_SCALED.get_rect().width,130))
    if rel_x < WIDTH:
        WIN.blit(FLOOR1_IMAGE_SCALED, (rel_x, 130))

    #WIN.blit(KNIGHTfs1, (100, 100))
    #WIN.blit(KNIGHTfs2, (100, 200))
    #WIN.blit(KNIGHTfs3, (100, 300))
    #WIN.blit(KNIGHTfs4, (100, 400))
    #WIN.blit(KNIGHTs1, (200, 100))
    #WIN.blit(KNIGHTs2, (200, 200))
    #WIN.blit(KNIGHTs3, (200, 300))
    #WIN.blit(KNIGHTs4, (200, 400))
    #WIN.blit(KNIGHTbs1, (200, 100))
    #WIN.blit(KNIGHTsws1, (200, 200))
    #WIN.blit(KNIGHTsws2, (200, 300))
    #WIN.blit(KNIGHTsws3, (200, 400))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    #positions = myfont.render("Playerposx: " + str(playerPosX) + " knightposx: " + str(knightPosX) + "stagePosX" + str(stagePosX), False, (0, 0, 0))
    #WIN.blit(positions,(0,100))
    healthtext = myfont.render(str(player.health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))
    pygame.font.init()
    myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
    enemyhitbox = myfont2.render("enemy.x: " + str(enemyKnight.x) + " enemy.y: " + str(enemyKnight.y) + " knightrect.x " + str(player.knightrect.x) + " knightrect.y " + str(player.knightrect.y), False, (0, 0, 0))
    WIN.blit(enemyhitbox,(0,100))
    healthtext = myfont.render(str(player.health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))

    # = pygame.draw.rect(surface, color, rect)
    player1healthbar = pygame.draw.rect(WIN, (255, 52, 25), (10, 10, player.health*2 , 40))
    enemy1healthbar = pygame.draw.rect(WIN, (255, 52, 25), (WIDTH-210, 10, enemy.health*2 , 40))
    deathtext = myfont.render("You died!", False, (255, 17, 0), )

    text_width = deathtext.get_width()
    text_height = deathtext.get_height()

    if not player.alive:
        pygame.draw.rect(WIN, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        WIN.blit(deathtext, (WIDTH/2 - text_width/2, HEIGHT/2 - text_height/2))
        #print (str(text_width))
        #print (str(text_height))

    #pygame.draw.rect(WIN, (100, 100, 100), (knightPosX, knight.y, KNIGHT_WIDTH, KNIGHT_HEIGHT))
    #pygame.draw.rect(WIN, (100, 100, 100), (enemy.x, enemy.y, ENEMY_WIDTH, ENEMY_HEIGHT))
    #pygame.draw.rect(WIN, (100, 100, 100), (enemy.x, enemy.y, 500, 200))
    #WIN.blit(knightrect)
    #else:
        #print("else")



    pygame.display.update()
if __name__ == "__main__":
    main()
