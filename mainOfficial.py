import pygame
import os
import time

#HW: make same thing as we did for player, for the enemy, make method for enemyRange and other function, (loading images, animations), work on jump
#HW do image load, try to fix it, maybe make new animation if you can't do anything else

#HW try to figure out why nothing is displaying
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 5

FLOOR1 = pygame.image.load(os.path.join('Assets', 'Floor.png'))
FLOOR1_IMAGE_SCALED = pygame.transform.scale(FLOOR1, (900, 400))

BACKGROUND = pygame.image.load(os.path.join('Assets', 'Background2.png'))
BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

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
        self.velocity = 0

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
# print("player")
# print(player.walkCount)
# print(player.playerPosX)
# print("------------------------------")
enemy = Enemy()
# print("enemy")
# print(enemy.walkCount)
# print(enemy.at500)
#
# player.playerPosX += 100
# print(player.playerPosX)

#loadimages
knight1_right = player.loadImage('Assets', 'Default_Character1N.png', player.knight_width, player.knight_height)
knight2_right = player.loadImage('Assets', 'Default_Character2.png', player.knight_width, player.knight_height)
knight3_right = player.loadImage('Assets', 'Default_Character3.png', player.knight_width, player.knight_height)
knight4_right = player.loadImage('Assets', 'Default_Character4.png', player.knight_width, player.knight_height)

knight1_left = player.loadImage('Assets', 'Default_Character_Flipped1.png', player.knight_width, player.knight_height)
knight2_left = player.loadImage('Assets', 'Default_Character_Flipped2.png', player.knight_width, player.knight_height)
knight3_left = player.loadImage('Assets', 'Default_Character_Flipped3.png', player.knight_width, player.knight_height)
knight4_left = player.loadImage('Assets', 'Default_Character_Flipped4.png', player.knight_width, player.knight_height)

knightSwing1_right = player.loadImage('Assets', 'Default_Character_Swing1.png', player.knight_width, player.knight_height)
knightSwing2_right = player.loadImage('Assets', 'Default_Character_Swing2.png', player.knight_width, player.knight_height)
knightSwing3_right = player.loadImage('Assets', 'Default_Character_Swing3.png', player.knight_width, player.knight_height)

knightBlock1_right = player.loadImage('Assets', 'Default_Character_Block1.png', 100, 100)

enemy1_right = enemy.loadImage('Assets', 'enemy.png', 100, 100)

#Rectangles defined
knightRect = pygame.Rect(player.knightPosX, 0, player.knight_width, player.knight_height)
knight = pygame.Rect(WIDTH/2 - player.knight_width, 0, player.knight_width, player.knight_height)

enemyKnight = pygame.Rect(WIDTH/2 - enemy.enemy_width, HEIGHT-FLOOR.height-enemy.enemy_height, enemy.enemy_width, enemy.enemy_height)
enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)

#Procedural variables
bgWidth, bgHeight = BACKGROUND_IMAGE_SCALED.get_rect().size
flWidth, flHeight = FLOOR1_IMAGE_SCALED.get_rect().size

Character_Movements = [pygame.image.load(os.path.join('Assets', 'Default_Character1N.png')), pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png')), pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))]

stageWidth = bgWidth*2
startScrollingPosX = (WIDTH / 2)
halfW = 37.5
global x
x = 0

#Lists defined
walkLeft = [knight1_left, knight2_left, knight3_left, knight4_left]
walkRight = [knight1_right, knight2_right, knight3_right, knight4_right]
swingRight = [knightSwing1_right, knightSwing2_right, knightSwing3_right]

#functions
def handle_movement(keys_pressed, knight):
    if pygame.key.get_pressed()[pygame.K_a]:
        player.velocity = -5
        player.left = True
        player.right = False
        player.still = False

    elif pygame.key.get_pressed()[pygame.K_d]:
        player.velocity = 5
        player.left = False
        player.right = True
        player.still = False

    else:
        player.still = True
        player.walkCount = 0

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



    player.playerPosX += player.velocity

    if player.playerPosX > stageWidth:
         player.playerPosX = stageWidth
         #makes right boundary

    if player.playerPosX < 0:
          player.playerPosX = 0
          #makes left boundary
    if player.playerPosX < startScrollingPosX - knight.width:
          player.knightPosX = player.playerPosX
          #if the screen doesn't need to scroll then the knight can move freely
    elif player.playerPosX > stageWidth - startScrollingPosX:
          player.knightPosX = player.playerPosX - stageWidth + WIDTH - knight.width
          #playerPosX = stageWidth + WIDTH
          #right boundary
    else:
          #playerPosX = startScrollingPosX - knight.width
          player.knightPosX = startScrollingPosX - knight.width
          player.stagePosX += player.velocity

    player.knightrect = pygame.Rect(player.knightPosX, knight.y, player.knight_width, player.knight_height)

def enemyMovement(enemyKnight):
    global knight
    velocity = 2
    rightOfKnight = True
    leftOfKnight = False

    if enemyKnight.x > knight.x:
        rightOfKnight = True
    elif enemyKnight.x < knight.x:
        leftOfKnight = True


def main():
    print("2")
    run = True
    clock = pygame.time.Clock()
    while run:
        if knight.y > HEIGHT - FLOOR.height - player.knight_height:
        #checking if knight is on ground
            player.jumping = False
        if knight.y < HEIGHT - FLOOR.height - player.knight_height:
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
        print("3")
        draw_window()
        handle_movement(keys_pressed, knight)
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

def draw_window():
    print("4")
    global x

    rel_x = player.stagePosX % BACKGROUND_IMAGE_SCALED.get_rect().width
    print("5")
    WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width,0))
    print("6")
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

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    #positions = myfont.render("Playerposx: " + str(playerPosX) + " knightposx: " + str(knightPosX) + "stagePosX" + str(stagePosX), False, (0, 0, 0))
    #WIN.blit(positions,(0,100))
    healthtext = myfont.render(str(player.health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))
    pygame.font.init()
    myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
    #enemyhitbox = myfont2.render("enemy.x: " + str(enemyKnight.x) + " enemy.y: " + str(enemyKnight.y) + " knightrect.x " + str(knightrect.x) + " knightrect.y " + str(knightrect.y), False, (0, 0, 0))
    #WIN.blit(enemyhitbox,(0,100))
    #healthtext = myfont.render(str(player.health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))

    player1healthbar = pygame.draw.rect(WIN, (255, 52, 25), (10, 10, player.health*2 , 40))
    enemy1healthbar = pygame.draw.rect(WIN, (255, 52, 25), (WIDTH-210, 10, enemy.health*2 , 40))
    deathtext = myfont.render("You died!", False, (255, 17, 0), )

    text_width = deathtext.get_width()
    text_height = deathtext.get_height()

    if not player.alive:
        pygame.draw.rect(WIN, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        WIN.blit(deathtext, (WIDTH/2 - text_width/2, HEIGHT/2 - text_height/2))


if __name__ == "__main__":
    print("1")
    main()
