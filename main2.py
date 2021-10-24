import pygame
import os
import time
import math

'''
HOMEWORK SECTION design character animations with bow, fix power, see if you can shoot multiple arrows, look into pools in skype
'''

# Screen Settings
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 200

# Floor
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
FLOOR1 = pygame.image.load(os.path.join('Assets', 'Floor.png'))
FLOOR1_IMAGE_SCALED = pygame.transform.scale(FLOOR1, (900, 400))
flWidth, flHeight = FLOOR1_IMAGE_SCALED.get_rect().size

# Background
BACKGROUND = pygame.image.load(os.path.join('Assets', 'Background2.png'))
BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
bgWidth, bgHeight = BACKGROUND_IMAGE_SCALED.get_rect().size
stageWidth = bgWidth*2
startScrollingPosX = (WIDTH / 2)


# Scrolling Background
# TODO: be more descriptive with variable names
#       scrolling_bg_x
global x
x = 0

arrow_x = 0
arrow_y = 0
global time
time = 0
power = 0
angle = 0
global shoot
shoot = False


class Character(object):
    def __init__(self):
        self.walkCount = 0
        self.swingCount = 0
        self.swingTrigger = False
        self.blockTrigger = False
        self.shootTrigger = False
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
        self.spikesX = 600
        self.platformX = 300
        self.arrowX = 0
        self.arrowY = 0
        self.beingStoppedRight = False
        self.beingStoppedLeft = False
        self.arrowShow = False
        self.hasBow = False
        self.bowActive = False
        self.swordActive = True

        Character.__init__(self)

class Enemy(Character):
    def __init__(self):
        self.at500 = False
        self.enemy_width = 100
        self.enemy_height = 100
        self.enemy_left = True
        self.enemy_right = False
        self.enemy_swinging = False
        self.enemyPosX = WIDTH/2 - self.enemy_width
        Character.__init__(self)

class Arrow():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, WIN):
        pygame.draw.circle(WIN, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def arrowpath(startX, startY, power, ang, time):
        angle = ang
        velX = math.cos(angle) * power
        velY = math.sin(angle) * power

        distX = velX * time
        distY = (velY * time) + ((-4.9 * (time)**2) / 2)

        newX = round(distX + startX)
        # print("x:", newX)
        newY = round(startY - distY)
        # print("y:", newY)
        return(newX, newY)

# print statements for testing
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

# loadimages

tree = player.loadImage(
'Assets', 'Tree.png', 130, 150)
knight1_right = player.loadImage(
    'Assets', 'Default_Character1N.png', player.knight_width, player.knight_height)
knight2_right = player.loadImage(
    'Assets', 'Default_Character2.png', player.knight_width, player.knight_height)
knight3_right = player.loadImage(
    'Assets', 'Default_Character3.png', player.knight_width, player.knight_height)
knight4_right = player.loadImage(
    'Assets', 'Default_Character4.png', player.knight_width, player.knight_height)

knight1_left = player.loadImage(
    'Assets', 'Default_Character_Flipped1.png', player.knight_width, player.knight_height)
knight2_left = player.loadImage(
    'Assets', 'Default_Character_Flipped2.png', player.knight_width, player.knight_height)
knight3_left = player.loadImage(
    'Assets', 'Default_Character_Flipped3.png', player.knight_width, player.knight_height)
knight4_left = player.loadImage(
    'Assets', 'Default_Character_Flipped4.png', player.knight_width, player.knight_height)

knightSwing1_right = player.loadImage(
    'Assets', 'Default_Character_Swing1.png', player.knight_width, player.knight_height)
knightSwing2_right = player.loadImage(
    'Assets', 'Default_Character_Swing2.png', player.knight_width, player.knight_height)
knightSwing3_right = player.loadImage(
    'Assets', 'Default_Character_Swing3.png', player.knight_width, player.knight_height)

knightBlock1_right = player.loadImage(
    'Assets', 'Default_Character_Block_1.png', player.knight_width, player.knight_height)

knightSwing1_left = player.loadImage(
    'Assets', 'Default_Character_Swing_Flipped1.png', player.knight_width, player.knight_height)
knightSwing2_left = player.loadImage(
    'Assets', 'Default_Character_Swing_Flipped2.png', player.knight_width, player.knight_height)
knightSwing3_left = player.loadImage(
    'Assets', 'Default_Character_Swing_Flipped3.png', player.knight_width, player.knight_height)

knightBlock1_left = player.loadImage(
    'Assets', 'Default_Character_Block_Flipped1.png', player.knight_width, player.knight_height)

knightBow1_right = player.loadImage(
    'Assets', 'Default_Character_Bow1.png', player.knight_width, player.knight_height)
knightBow2_right = player.loadImage(
    'Assets', 'Default_Character_Bow2.png', player.knight_width, player.knight_height)
knightBow3_right = player.loadImage(
    'Assets', 'Default_Character_Bow3.png', player.knight_width, player.knight_height)
knightBow4_right = player.loadImage(
    'Assets', 'Default_Character_Bow4.png', player.knight_width, player.knight_height)

knightBow1_left = player.loadImage(
    'Assets', 'Default_Character_Bow_Flipped1.png', player.knight_width, player.knight_height)
knightBow2_left = player.loadImage(
    'Assets', 'Default_Character_Bow_Flipped2.png', player.knight_width, player.knight_height)
knightBow3_left = player.loadImage(
    'Assets', 'Default_Character_Bow_Flipped3.png', player.knight_width, player.knight_height)
knightBow4_left = player.loadImage(
    'Assets', 'Default_Character_Bow_Flipped4.png', player.knight_width, player.knight_height)

knightShoot_right = player.loadImage(
    'Assets', 'Default_Character_Shoot1.png', player.knight_width, player.knight_height)

knightShoot_left = player.loadImage(
    'Assets', 'Default_Character_Shoot_Flipped1.png', player.knight_width, player.knight_height)


enemy1_right = enemy.loadImage('Assets', 'enemy.png', 100, 100)

platform = player.loadImage('Assets', 'Platform.png', 100, 100)
spikes = player.loadImage('Assets', 'Spikes.png', 100, 100)
bow = player.loadImage('Assets', 'bow.png', 100, 100)
arrowImage = player.loadImage('Assets', 'Arrow.png', 70, 70)
sword = player.loadImage('Assets', 'Sword.png', 100, 100)

# Rectangles defined
'''
TODO: Can be defined in our loadImage method, may need to change though
'''


knightRect = pygame.Rect(player.knightPosX, 0,
                         player.knight_width, player.knight_height)
knight = pygame.Rect(WIDTH/2 - player.knight_width, 450-player.knight_height,
                     player.knight_width, player.knight_height)

enemyKnight = pygame.Rect(enemy.enemyPosX, HEIGHT-FLOOR.height -
                          enemy.enemy_height, enemy.enemy_width, enemy.enemy_height)


enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)

spikesRect = pygame.Rect(player.spikesX, 300, 80, 100)
bowRect = pygame.Rect(player.platformX - 10, 220, 100, 100)
arrow = Arrow(0, 0, 5, (255,255,255))


global b_spike
b_spike = spikesRect.x
global e_spike
e_spike = spikesRect.x + 80

spikesStartRect = pygame.Rect(b_spike, 383, 5, spikesRect.height)
spikesEndRect = pygame.Rect(e_spike, 383, 5, spikesRect.height)
spikesTopRect = pygame.Rect(player.spikesX + 5, 383, 75, 5)
#80
platformRect = pygame.Rect(player.platformX, 300, 100, 10)




Character_Movements = [
    pygame.image.load(os.path.join('Assets', 'Default_Character1N.png')),
    pygame.image.load(os.path.join(
        'Assets', 'Default_Character_Flipped1.png')),
    pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))]


# Lists defined
walkLeft = [knight1_left, knight2_left, knight3_left, knight4_left]
walkRight = [knight1_right, knight2_right, knight3_right, knight4_right]

walkLeftBow =[knightBow1_left, knightBow2_left, knightBow3_left, knightBow4_left]
walkRightBow = [knightBow1_right, knightBow2_right, knightBow3_right, knightBow4_right]

swingLeft = [knightSwing1_left, knightSwing2_left, knightSwing3_left]
swingRight = [knightSwing1_right, knightSwing2_right, knightSwing3_right]

# functions

def handle_movement(keys_pressed, knight):
    global b_spike
    global e_spike
    '''
    TODO: Add comments near if statements describing what is happening
    '''

    if pygame.key.get_pressed()[pygame.K_a] and not player.beingStoppedLeft:
        player.velocity = -5
        player.left = True
        player.right = False
        player.still = False
    #if press a move left
    elif pygame.key.get_pressed()[pygame.K_d] and not player.beingStoppedRight:
        player.velocity = 5
        player.left = False
        player.right = True
        player.still = False
    #if press d move right
    else:
        player.still = True
        player.walkCount = 0
        player.velocity = 0

    if not(player.jumping):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player.jumping = True
            player.walkCount = 0
    #if press space jump
    if player.jumping:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount <= 0:
                neg = -1
            # knight.y -= (player.jumpCount ** 2) * 0.5 * neg
            knight.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.jumping = False
            player.jumpCount = 10
            knight.y += 5

    # 1234
#jumpcount = 10, 9, 8, 7
#knight.y = 100, 140.5, 172.5, 197



# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7 -8, -9, -10
    player.playerPosX += player.velocity

    if player.playerPosX > stageWidth:
        player.playerPosX = stageWidth
        # makes right boundary

    if player.playerPosX < 0:
        player.playerPosX = 0
        # makes left boundary

    if player.playerPosX < startScrollingPosX - knight.width:
        player.knightPosX = player.playerPosX
        # enemy.enemyPosX = enemyKnight.x
        # if the screen doesn't need to scroll then the knight can move freely

    elif player.playerPosX > stageWidth - startScrollingPosX:
        player.knightPosX = player.playerPosX - stageWidth + WIDTH - knight.width
        # enemy.enemyPosX = enemyKnight.x - stageWidth + WIDTH - enemy.enemy_width
        # if you make it to the end you can walk normally
    else:
        player.knightPosX = startScrollingPosX - knight.width
        player.stagePosX += player.velocity
        enemyKnight.x -= player.velocity
        player.spikesX -= player.velocity
        spikesRect.x -= player.velocity
        b_spike -= player.velocity
        e_spike -= player.velocity
        player.platformX -= player.velocity
        platformRect.x -= player.velocity
        spikesStartRect.x -= player.velocity
        spikesEndRect.x -= player.velocity
        spikesTopRect.x -= player.velocity

        #middle boundary

    player.knightrect = pygame.Rect(
        player.knightPosX, knight.y, player.knight_width, player.knight_height)

# ####################################################################
#
# player.playerPosX += player.velocity
#
# if player.playerPosX > stageWidth:
#     player.playerPosX = stageWidth
#     # makes right boundary
#
# if player.playerPosX < 0:
#     player.playerPosX = 0
#     # makes left boundary
# if player.playerPosX < startScrollingPosX - knight.width:
#     player.knightPosX = player.playerPosX
#     # if the screen doesn't need to scroll then the knight can move freely
# elif player.playerPosX > stageWidth - startScrollingPosX:
#     player.knightPosX = player.playerPosX - stageWidth + WIDTH - knight.width
#     #playerPosX = stageWidth + WIDTH
#     # right boundary
# else:
#     #playerPosX = startScrollingPosX - knight.width
#     player.knightPosX = startScrollingPosX - knight.width
#     player.stagePosX += player.velocity
#
# player.knightrect = pygame.Rect(
#     player.knightPosX, knight.y, player.knight_width, player.knight_height)
#
# #######################################################

def moveAutomatically(b_range, e_range, velocity = 2):

    if player.knightPosX + knight.width > b_range and player.knightPosX < e_range:
        if player.knightPosX > enemyKnight.x:
            enemyKnight.x += velocity
        elif player.knightPosX < enemyKnight.x:
            enemyKnight.x -= velocity
    # else:
    #     if enemy.enemy_left:
    #         if enemyKnight.x < 0:
    #             enemy.enemy_right = True
    #             enemy.enemy_left = False
    #         enemyKnight.x -= velocity
    #     elif enemy.enemy_right:
    #         if enemyKnight.x > WIDTH - enemy.enemy_width:
    #             enemy.enemy_left = True
    #             enemy.enemy_right = False
    #         enemyKnight.x += velocity
def main():
    global shoot
    global time
    run = True
    clock = pygame.time.Clock()
    while run:
        if player.hasBow:
            # Hotbar = [True, False]
            if pygame.key.get_pressed()[pygame.K_1]:
                # Hotbar[0] = True
                # Hotbar[1] = False
                player.bowActive = False
                player.swordActive = True
            if pygame.key.get_pressed()[pygame.K_2]:
                # Hotbar[0] = False
                # Hotbar[1] = True
                player.bowActive = True
                player.swordActive = False

            # if Hotbar[0]:
            #     player.bowActive = False
            # elif Hotbar[1]:
            #     player.bowActive = True
        if shoot:
            if arrow.y < 500-FLOOR.height - arrow.radius and arrow.y > 0 and arrow.x > 0:
                player.arrowShow = True
                time += 0.05
                po = Arrow.arrowpath(arrow_x, arrow_y, power, angle, time)
                arrow.x = po[0]

                # print(po[0])
                arrow.y = po[1]

            else:
                # print("here")
                player.swingTrigger = False
                player.arrowShow = False
                shoot = False
                time = 0                # arrow.x = player.knightPosX
                # arrow.y = knight.y



        line = [(player.knightPosX, knight.y), pygame.mouse.get_pos()]
        # arrow.draw(WIN)
        # pygame.draw.line(WIN, (0,0,0), line[0], line[1])
        '''
        TODO: can you think of another place to move these if statements?
             May need to move
        '''
        #if knight.y > HEIGHT - FLOOR.height - player.knight_height:
            # checking if knight is on ground
            #player.jumping = False
        #if knight.y < HEIGHT - FLOOR.height - player.knight_height:
            # if knight is on ground dont apply gravity
            #knight.y += 5

            #print(HEIGHT - FLOOR.y)
        clock.tick(FPS)

        # Update display each frame
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.swinging = True
                    player.swingTrigger = True
                if shoot == False and player.bowActive:
                    player.shootTrigger = True
                    arrow.x = player.knightPosX + 20
                    arrow.y = knight.y + 50
                    arrow_x = arrow.x
                    arrow_y = arrow.y
                    pos = pygame.mouse.get_pos()
                    shoot = True
                    power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][1])**2)/3
                    #(mouse.y) - (arrow.y)^2 + (mouse.x) - (arrow.x)^2
                    angle = findAngle(pos)
                    #swingCount += 1
                    # handle_swing(swingTrigger)
                    #print("swingtrigger", swingTrigger)
                if event.button == 3:
                    player.blocking = True
                    player.blockTrigger = True
                    # handle_block(blockTrigger)
                    #print("blocktrigger", blockTrigger)




            else:
                player.blockTrigger = False


        keys_pressed = pygame.key.get_pressed()
        draw_window(line)
        handle_movement(keys_pressed, knight)
        handle_damage()
        handle_objects()
    pygame.quit()

def findAngle(pos):
    sX = arrow.x
    sY = arrow.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle

def handle_objects():
    if player.knightrect.colliderect(bowRect):
        player.hasBow = True

    if player.knightrect.colliderect(platformRect):
        knight.y = 235
    elif not player.jumping:
        if knight.y < HEIGHT-FLOOR.height:
            knight.y == HEIGHT-FLOOR.height
        if not player.knightrect.colliderect(platformRect) and knight.y < 383:
            knight.y += 15
        if knight.y > 383:
            knight.y = 383
    if player.knightrect.colliderect(spikesStartRect) and not player.knightrect.colliderect(spikesTopRect):
        player.beingStoppedRight = True
    else:
        player.beingStoppedRight = False

    if player.knightrect.colliderect(spikesEndRect) and not player.knightrect.colliderect(spikesTopRect):
        player.beingStoppedLeft = True
    else:
        player.beingStoppedLeft = False
    if player.knightrect.colliderect(spikesTopRect):
        knight.y = 320



def handle_damage():
    global enemyKnight
    if arrowRect.colliderect(enemyKnight):
        enemy.health -= 1
        print("hit")
    if player.knightrect.colliderect(enemyKnight) and not player.blockTrigger:
        ticks = pygame.time.get_ticks()
        if ticks%13 == 0 and enemy.enemy_swinging:
            enemy.enemy_swinging = True
            if enemy.enemy_swinging == True:
                if enemy.enemy_left:

                    # WIN.blit(swingLeft[player.swingCount//3],
                    #          (player.knightPosX, knight.y))
                    enemy.swingCount += 1
                    if enemy.swingCount//3 > 2:
                        enemy.swingCount = 0
                        player.health -= 1
                        enemy.enemy_swinging = False
                elif enemy.enemy_right:
                    # WIN.blit(swingRight[player.swingCount//3],
                    #          (player.knightPosX, knight.y))
                    enemy.swingCount += 1
                    if enemy.swingCount//3 > 2:
                        enemy.swingCount = 0
                        player.health -= 1
                        enemy.enemy_swinging = False

    if enemyKnight.colliderect(player.knightrect) and player.swingTrigger and player.swordActive:
        enemy.health -= 1
        print("1")

    # if enemyKnight.colliderect(player.knightrect):
    #     enemy.enemy_swinging = True

    if player.health == 0:
        print("player dead")
        player.alive = False
    if enemy.health == 0:
        enemyKnight.x = 0
        enemyKnight.y = 5000
        enemy.alive = False

    if spikesRect.colliderect(player.knightrect) and not player.blockTrigger:
        player.health -= 0.1
    # if spikesStartRect.colliderect(player.knightRect)
    #     knightR

def draw_window(line):
    global x
    global newX
    global newY
    rel_x = player.stagePosX % BACKGROUND_IMAGE_SCALED.get_rect().width
    WIN.blit(BACKGROUND_IMAGE_SCALED,
             (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width, 0))
    if rel_x < WIDTH:
        WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))
    x -= 1

    if enemy.alive:
        WIN.blit(enemy1_right, (enemyKnight.x, HEIGHT - FLOOR.height - enemy.enemy_height))
        moveAutomatically(enemyKnight.x - 100 ,enemyKnight.x + enemy.enemy_width + 100)
#qwerty



    b_range = enemyKnight.x - 50
    e_range = enemyKnight.x + enemy.enemy_width + 50
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(b_range, 0, 5, HEIGHT))
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(e_range, 0, 5, HEIGHT))

    pygame.draw.rect(WIN, (255, 52, 25), (WIDTH-210, 10, enemy.health*2, 40))
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(player.platformX, 300, 100, 10))

    # pygame.draw.rect(WIN, (0,0,0), pygame.Rect(b_spike, 383, 5, spikesRect.height))
    # pygame.draw.rect(WIN, (0,0,0), pygame.Rect(e_spike, 383, 5, spikesRect.height))
    # pygame.draw.rect(WIN, (0,0,0), pygame.Rect(player.spikesX, 383, 80, 5))
    if player.swordActive:
        if player.walkCount + 1 >= 30:
            player.walkCount = 0

        if not(player.still):
            if player.left:
                WIN.blit(walkLeft[player.walkCount//10],
                         (player.knightPosX, knight.y))
                player.walkCount += 1
            elif player.right:
                WIN.blit(walkRight[player.walkCount//10],
                         (player.knightPosX, knight.y))
                player.walkCount += 1

        elif player.swingTrigger == True:
            if player.left:
                WIN.blit(swingLeft[player.swingCount//3],
                         (player.knightPosX, knight.y))
                player.swingCount += 1
                if player.swingCount//3 > 2:
                    player.swingCount = 0
                    player.swingTrigger = False
            elif player.right:
                WIN.blit(swingRight[player.swingCount//3],
                         (player.knightPosX, knight.y))
                player.swingCount += 1
                if player.swingCount//3 > 2:
                    player.swingCount = 0
                    player.swingTrigger = False


        elif player.blockTrigger == True:
            if player.right:
                WIN.blit(knightBlock1_right, (player.knightPosX, knight.y))
            elif player.left:
                WIN.blit(knightBlock1_left, (player.knightPosX, knight.y))
            #blockTrigger = False
            #print(blockTrigger, "b")

        elif player.still:
            if player.right:
                WIN.blit(walkRight[0], (player.knightPosX, knight.y))
            elif player.left:
                WIN.blit(walkLeft[0], (player.knightPosX, knight.y))

        if pygame.key.get_pressed()[pygame.K_SPACE] and player.jumping == False:
            pass

####################################################################################

    elif player.bowActive:
        if player.walkCount + 1 >= 30:
            player.walkCount = 0

        if not(player.still):
            if player.left:
                WIN.blit(walkLeftBow[player.walkCount//10],
                         (player.knightPosX, knight.y))
                player.walkCount += 1
            elif player.right:
                WIN.blit(walkRightBow[player.walkCount//10],
                         (player.knightPosX, knight.y))
                player.walkCount += 1

        elif player.swingTrigger == True:
            if player.left:
                WIN.blit(knightShoot_left, (player.knightPosX, knight.y))

            elif player.right:
                WIN.blit(knightShoot_right, (player.knightPosX, knight.y))


        elif player.still:
            if player.right:
                WIN.blit(walkRightBow[0], (player.knightPosX, knight.y))
            elif player.left:
                WIN.blit(walkLeftBow[0], (player.knightPosX, knight.y))

        if pygame.key.get_pressed()[pygame.K_SPACE] and player.jumping == False:
            pass




    WIN.blit(FLOOR1_IMAGE_SCALED,
             (rel_x - FLOOR1_IMAGE_SCALED.get_rect().width, 130))
    if rel_x < WIDTH:
        WIN.blit(FLOOR1_IMAGE_SCALED, (rel_x, 130))

        WIN.blit(spikes, (player.spikesX, 350))


    '''
    TODO: Create a separate function that displays text
    something like
    i.e. def renderText(text, posX, posY)
    '''

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    #positions = myfont.render("Playerposx: " + str(playerPosX) + " knightposx: " + str(knightPosX) + "stagePosX" + str(stagePosX), False, (0, 0, 0))
    # WIN.blit(positions,(0,100))
    healthtext = myfont.render(f"spikesRect.x: {spikesRect.x} spikesRect.y: {spikesRect.y} spikesX; {player.spikesX} b_spike: {b_spike} e_spike: {e_spike}", False, (0, 0, 0))
    positiontext = myfont.render(f"stagePosx: {player.stagePosX} Playerposx: {player.playerPosX} KnightPosX: {player.knightPosX} EnemyPosX: {enemy.enemyPosX} knight.y: {knight.y}", False, (0, 0, 0))
    collidetext = myfont.render(f"spikesTopRect.x: {spikesTopRect.x} spikesTopRect.y: {spikesTopRect.y}", False, (0,0,0))
    arrowtext = myfont.render(f"arrow.x {arrow.x} arrow.y {arrow.y} power: {(((pygame.mouse.get_pos()[1]) - (knight.y))**2 + ((pygame.mouse.get_pos()[0]) - (player.knightPosX))**2)/8}", False, (0,0,0))
    global arrowRect
    arrowRect = pygame.Rect(arrow.x, arrow.y, 100, 10)

    # WIN.blit(collidetext, (0,100))
    # WIN.blit(positiontext, (0,200))
    WIN.blit(arrowtext, (0, 100))
    WIN.blit(positiontext, (0, 200))
    pygame.font.init()
    myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
    #enemyhitbox = myfont2.render("enemy.x: " + str(enemyKnight.x) + " enemy.y: " + str(enemyKnight.y) + " knightrect.x " + str(knightrect.x) + " knightrect.y " + str(knightrect.y), False, (0, 0, 0))
    # WIN.blit(enemyhitbox,(0,100))
    #healthtext = myfont.render(str(player.health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))

    player1healthbar = pygame.draw.rect(
        WIN, (255, 52, 25), (10, 10, player.health*2, 40))
    enemy1healthbar = pygame.draw.rect(
        WIN, (255, 52, 25), (WIDTH-210, 10, enemy.health*2, 40))
    deathtext = myfont.render("You died!", False, (255, 17, 0), )

    text_width = deathtext.get_width()
    text_height = deathtext.get_height()

    WIN.blit(platform, (player.platformX, 300, 100, 10))
    if not player.hasBow:
        WIN.blit(bow, (player.platformX - 10, 220, 100, 100))
    if player.arrowShow:
        WIN.blit(arrowImage, (arrow.x-35, arrow.y-35, 10, 10))

    if player.health <= 0:
        pygame.draw.rect(WIN, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        WIN.blit(deathtext, (WIDTH/2 - text_width/2, HEIGHT/2 - text_height/2))

    # pygame.draw.rect(WIN, (0,0,0), (player.arrowX, player.arrowY, 100, 10))
    if not player.hasBow:
        pygame.draw.rect(WIN, (156, 152, 142), (WIDTH/2 - 40, HEIGHT - 45, 40, 40))
        pygame.draw.rect(WIN, (217, 211, 210), (WIDTH/2 - 40, HEIGHT - 45, 40, 40), 3)
        swordScaled = pygame.transform.scale(sword, (210, 210))
        WIN.blit(swordScaled, (WIDTH/2 - 30, HEIGHT - 42, 40, 40))
    if player.hasBow:
        pygame.draw.rect(WIN, (156, 152, 142), (WIDTH/2 - 70, HEIGHT - 45, 40, 40))
        if player.bowActive:
            pygame.draw.rect(WIN, (130, 127, 118), (WIDTH/2 - 70, HEIGHT - 45, 40, 40), 3)
        elif player.swordActive:
            pygame.draw.rect(WIN, (217, 211, 210), (WIDTH/2 - 70, HEIGHT - 45, 40, 40), 3)

        pygame.draw.rect(WIN, (156, 152, 142), (WIDTH/2 - 10, HEIGHT - 45, 40, 40))
        if player.bowActive:
            pygame.draw.rect(WIN, (217, 211, 210), (WIDTH/2 - 10, HEIGHT - 45, 40, 40), 3)
        elif player.swordActive:
            pygame.draw.rect(WIN, (156, 152, 142), (WIDTH/2 - 10, HEIGHT - 45, 40, 40), 3)
        bowScaled = pygame.transform.scale(bow, (70, 70))
        WIN.blit(bowScaled, (WIDTH/2 - 37, HEIGHT - 60, 40, 40))
        swordScaled = pygame.transform.scale(sword, (210, 210))
        WIN.blit(swordScaled, (WIDTH/2 - 59, HEIGHT - 42, 40, 40))

if __name__ == "__main__":
    main()
