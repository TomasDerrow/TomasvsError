import pygame
import os
import time
#HW - clean up code, use the guy's code as insparation for walking animation
pygame.init()
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
#pygame.Surface.set_colorkey(KNIGHT_IMAGE, [255,255,255])

KNIGHT_WIDTH, KNIGHT_HEIGHT = 75, 67
ENEMY_WIDTH, ENEMY_HEIGHT = 100, 100
knight = pygame.Rect(WIDTH/2 - KNIGHT_WIDTH, 0, KNIGHT_WIDTH, KNIGHT_HEIGHT)


KNIGHT1 = pygame.image.load(os.path.join('Assets', 'Default_Character1.png'))
KNIGHT2 = pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))
KNIGHT3 = pygame.image.load(os.path.join('Assets', 'Default_Character3.png'))
KNIGHT4 = pygame.image.load(os.path.join('Assets', 'Default_Character4.png'))

KNIGHTf1 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png'))
KNIGHTf2 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped2.png'))
KNIGHTf3 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped3.png'))
KNIGHTf4 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped4.png'))


KNIGHTs1 = pygame.transform.scale(KNIGHT1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTs2 = pygame.transform.scale(KNIGHT2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTs3 = pygame.transform.scale(KNIGHT3, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTs4 = pygame.transform.scale(KNIGHT4, (KNIGHT_WIDTH, KNIGHT_HEIGHT))

KNIGHTfs1 = pygame.transform.scale(KNIGHTf1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTfs2 = pygame.transform.scale(KNIGHTf2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTfs3 = pygame.transform.scale(KNIGHTf3, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHTfs4 = pygame.transform.scale(KNIGHTf4, (KNIGHT_WIDTH, KNIGHT_HEIGHT))


ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemy.png'))
ENEMY_IMAGE_SCALED = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))
enemy = pygame.Rect(WIDTH/2 - ENEMY_WIDTH, 0, ENEMY_WIDTH, ENEMY_HEIGHT)
transparent = (0, 0, 0, 0)
#Background scrolling
BACKGROUND = pygame.image.load(os.path.join('Assets', 'Background2.png'))
BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
bgWidth, bgHeight = BACKGROUND_IMAGE_SCALED.get_rect().size

Character_Movements = [pygame.image.load(os.path.join('Assets', 'Default_Character1.png')), pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png')), pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))]

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

FLOOR1 = pygame.image.load(os.path.join('Assets', 'Floor.png'))
FLOOR1_IMAGE_SCALED = pygame.transform.scale(FLOOR1, (900, 400))
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
global middle
middle = False
global end
end = False
walkLeft = [KNIGHTfs1, KNIGHTfs2, KNIGHTfs3, KNIGHTfs4]
walkRight = [KNIGHTs1, KNIGHTs2, KNIGHTs3, KNIGHTs4]

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
        knight.y -= 150



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
          end = True
          #playerPosX = stageWidth + WIDTH
          #print("here12")
          #right boundary
    else:
          #playerPosX = startScrollingPosX - knight.width
          knightPosX = startScrollingPosX - knight.width

          stagePosX += playerVelocityX
          middle = True
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
    velocity = 2

    #totalMoved = 0
    if enemy.x < 500 and at500 == False:
        enemy.x += velocity
        #totalMoved += velocity
    elif enemy.x > 50:
        enemy.x -= velocity
        at500 = True
    else:
        at500 = False



#game loop
def main():
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

        keys_pressed = pygame.key.get_pressed()
        draw_window()
        handle_movement(keys_pressed, knight, playerVelocityX)
        enemyMovement(enemy)

    pygame.quit()

#drawing all assets
def draw_window():
    global LEFT
    global RIGHT
    global walkCount
    global STILL
    global x
    global middle


    rel_x = stagePosX % BACKGROUND_IMAGE_SCALED.get_rect().width
    WIN.fill((52,192,235))
    WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width,0))
    if rel_x < WIDTH:
         WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))
    x -= 1
    pygame.draw.rect(WIN, (66,245,84), FLOOR)
    #WIN.blit(KNIGHT_IMAGE_SCALED1, (playerPosX, knight.y))
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
    else:
        if RIGHT:
            WIN.blit(walkRight[0], (knightPosX, knight.y))
        elif LEFT:
            WIN.blit(walkLeft[0], (knightPosX, knight.y))

    if pygame.key.get_pressed()[pygame.K_SPACE] and JUMPING == False:
        print("3")
    WIN.blit(FLOOR1_IMAGE_SCALED, (0, 130))

    #WIN.blit(KNIGHTfs1, (100, 100))
    #WIN.blit(KNIGHTfs2, (100, 200))
    #WIN.blit(KNIGHTfs3, (100, 300))
    #WIN.blit(KNIGHTfs4, (100, 400))
    #WIN.blit(KNIGHTs1, (200, 100))
    #WIN.blit(KNIGHTs2, (200, 200))
    #WIN.blit(KNIGHTs3, (200, 300))
    #WIN.blit(KNIGHTs4, (200, 400))

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render("Playerposx: " + str(playerPosX) + " knightposx: " + str(knightPosX) + "stagePosX" + str(stagePosX), False, (0, 0, 0))
    WIN.blit(textsurface,(0,100))

    if middle:
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("reached middle", False, (0, 0, 0))
        WIN.blit(textsurface,(0,50))

    if end:
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("reached end", False, (0, 0, 0))
        WIN.blit(textsurface,(100,50))
    #else:
        #print("else")



    pygame.display.update()
if __name__ == "__main__":
    main()
