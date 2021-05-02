import pygame
import os
import time
#HW - draw flipped blocking and swinging animations, be able to swing while walking
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 5
global at500
at500 = False
global walkCount
walkCount = 0
global swingCount
swingCount = 0
global swingTrigger
swingTrigger = False
global blockTrigger
blockTrigger = False
global enemyalive
enemyalive = True
global playeralive
playeralive = True

global health
health = 100
enemyhealth = 100
#pygame.Surface.set_colorkey(KNIGHT_IMAGE, [255,255,255])

KNIGHT_WIDTH, KNIGHT_HEIGHT = 75, 67
ENEMY_WIDTH, ENEMY_HEIGHT = 100, 100


knight = pygame.Rect(WIDTH/2 - KNIGHT_WIDTH, 0, KNIGHT_WIDTH, KNIGHT_HEIGHT)
global enemy
enemy = pygame.Rect(WIDTH/2 - ENEMY_WIDTH, HEIGHT-FLOOR.height-ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT)


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

ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemy.png'))
ENEMY_IMAGE_SCALED = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))
transparent = (0, 0, 0, 0)
#Background scrolling
BACKGROUND = pygame.image.load(os.path.join('Assets', 'Background2.png'))
BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
bgWidth, bgHeight = BACKGROUND_IMAGE_SCALED.get_rect().size

FLOOR1 = pygame.image.load(os.path.join('Assets', 'Floor.png'))
FLOOR1_IMAGE_SCALED = pygame.transform.scale(FLOOR1, (900, 400))
flWidth, flHeight = FLOOR1_IMAGE_SCALED.get_rect().size
Character_Movements = [pygame.image.load(os.path.join('Assets', 'Default_Character1N.png')), pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png')), pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))]

stageWidth = bgWidth*2
global stagePosX
stagePosX = 0

startScrollingPosX = (WIDTH / 2)

halfW = 37.5
global knightPosX
knightPosX = halfW

global playerPosX
playerPosX = halfW
#playerPosY = 500
playerVelocityX = 0

global knightrect
knightrect = pygame.Rect(knightPosX, knight.y, KNIGHT_WIDTH, KNIGHT_HEIGHT)

global enemyRange
enemyRange = pygame.Rect(enemy.x, enemy.y, 500, 200)

global x
x = 0
global JUMPING
JUMPING = False

global LEFT
LEFT = False
global RIGHT
RIGHT = True
global STILL
STILL = True
global Swinging
Swinging = False
global Blocking
Blocking = False

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
    global JUMPING
    global playerPosX
    global stagePosX
    global knightPosX
    global LEFT
    global RIGHT
    global STILL
    global middle
    global end
    global health
    global knightrect
    #global playerPosY

    if pygame.key.get_pressed()[pygame.K_a]:
        playerVelocityX = -5
        LEFT = True
        RIGHT = False
        STILL = False

    elif pygame.key.get_pressed()[pygame.K_d]:
        playerVelocityX = 5
        LEFT = False
        RIGHT = True
        STILL = False
        #KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'Default_Character.png'))
    #RIGHT
    else:
        STILL = True
        walkCount = 0

    if pygame.key.get_pressed()[pygame.K_SPACE] and JUMPING == False:
        JUMPING = True
        knight.y -= 400





    playerPosX += playerVelocityX

    if playerPosX > stageWidth:
         playerPosX = stageWidth
         #makes right boundary

    if playerPosX < 0:
          playerPosX = 0
          #makes left boundary
    if playerPosX < startScrollingPosX - knight.width:
          knightPosX = playerPosX
         # print("here1")
          #if the screen doesn't need to scroll then the knight can move freely
    elif playerPosX > stageWidth - startScrollingPosX:
          knightPosX = playerPosX - stageWidth + WIDTH - knight.width
          #playerPosX = stageWidth + WIDTH
          #print("here12")
          #right boundary
    else:
          #playerPosX = startScrollingPosX - knight.width
          knightPosX = startScrollingPosX - knight.width
          stagePosX += playerVelocityX

    global knightrect
    knightrect = pygame.Rect(knightPosX, knight.y, KNIGHT_WIDTH, KNIGHT_HEIGHT)
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


def enemyMovement(enemy):
    global at500
    global knight
    velocity = 2
    rightOfKnight = True
    leftOfKnight = False

    if enemy.x > knight.x:
        rightOfKnight = True
    elif enemy.x < knight.x:
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
    global swingTrigger
    global blockTrigger
    global swingCount
    run = True
    clock = pygame.time.Clock()
    while run:
        if knight.y > HEIGHT - FLOOR.height - KNIGHT_HEIGHT:
        #checking if knight is on ground
            global JUMPING
            JUMPING = False
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
                    Swinging = True
                    swingTrigger = True
                    #swingCount += 1
                    #handle_swing(swingTrigger)
                    #print("swingtrigger", swingTrigger)
                if event.button == 3:
                    Blocking = True
                    blockTrigger = True
                    #handle_block(blockTrigger)
                    #print("blocktrigger", blockTrigger)

            else:
                blockTrigger = False

        keys_pressed = pygame.key.get_pressed()
        draw_window()
        handle_movement(keys_pressed, knight, playerVelocityX)
        enemyMovement(enemy)
        handle_damage()

    pygame.quit()

def handle_damage():
    global health
    global enemyhealth
    global playerPosX
    global knightrect
    global enemy
    global blockTrigger
    global enemyalive
    global playeralive

    if knightrect.colliderect(enemy) and not blockTrigger:
        health -= 0.1
    if enemy.colliderect(knightrect) and swingTrigger:
        enemyhealth -= 1

    if health == 0:
        print("player dead")
        playeralive = False
    if enemyhealth == 0:
        enemy.x = 0
        enemy.y = 5000
        enemyalive = False




#drawing all assets
def draw_window():
    global LEFT
    global RIGHT
    global walkCount
    global STILL
    global x
    global middle
    global Swinging
    global Blocking
    global swingTrigger
    global blockTrigger
    global swingCount
    global enemyalive
    global playeralive
    global enemyRange

    rel_x = stagePosX % BACKGROUND_IMAGE_SCALED.get_rect().width
    WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width,0))
    if rel_x < WIDTH:
         WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))
    x -= 1

    if enemyalive:
        WIN.blit(ENEMY_IMAGE_SCALED, (enemy.x, HEIGHT - FLOOR.height - ENEMY_HEIGHT))

    if walkCount + 1 >= 30:
        walkCount = 0

    if not(STILL):
        if LEFT:
            WIN.blit(walkLeft[walkCount//10], (knightPosX, knight.y))
            walkCount += 1
        elif RIGHT:
            WIN.blit(walkRight[walkCount//10], (knightPosX, knight.y))
            walkCount += 1

    elif swingTrigger == True:
        WIN.blit(swingRight[swingCount//3], (knightPosX, knight.y))
        swingCount += 1
        if swingCount//3 > 2:
            swingCount = 0
            swingTrigger = False

    elif blockTrigger == True:
        WIN.blit(KNIGHTbs1, (knightPosX, knight.y))

        #blockTrigger = False
        #print(blockTrigger, "b")

    elif STILL:
        if RIGHT:
            WIN.blit(walkRight[0], (knightPosX, knight.y))
        elif LEFT:
            WIN.blit(walkLeft[0], (knightPosX, knight.y))



    if pygame.key.get_pressed()[pygame.K_SPACE] and JUMPING == False:
        print("3")


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
    healthtext = myfont.render(str(health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))
    pygame.font.init()
    myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
    enemyhitbox = myfont2.render("enemy.x: " + str(enemy.x) + " enemy.y: " + str(enemy.y) + " knightrect.x " + str(knightrect.x) + " knightrect.y " + str(knightrect.y), False, (0, 0, 0))
    WIN.blit(enemyhitbox,(0,100))
    healthtext = myfont.render(str(health), False, (0, 0, 0))
    #WIN.blit(healthtext, (200,20))

    # = pygame.draw.rect(surface, color, rect)
    player1healthbar = pygame.draw.rect(WIN, (255, 52, 25), (10, 10, health*2 , 40))
    enemy1healthbar = pygame.draw.rect(WIN, (255, 52, 25), (WIDTH-210, 10, enemyhealth*2 , 40))
    deathtext = myfont.render("You died!", False, (255, 17, 0), )

    text_width = deathtext.get_width()
    text_height = deathtext.get_height()

    if not playeralive:
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
