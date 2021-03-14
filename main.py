import pygame
import os
import time
#HW - fix scrolling background, try to figure out walking animation
pygame.init()
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 5
global at500
at500 = False
#pygame.Surface.set_colorkey(KNIGHT_IMAGE, [255,255,255])

KNIGHT_WIDTH, KNIGHT_HEIGHT = 75, 67
ENEMY_WIDTH, ENEMY_HEIGHT = 100, 100
knight = pygame.Rect(WIDTH/2 - KNIGHT_WIDTH, 0, KNIGHT_WIDTH, KNIGHT_HEIGHT)


KNIGHT_IMAGE1 = pygame.image.load(os.path.join('Assets', 'Default_Character1.png'))
KNIGHT_IMAGE2 = pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))
KNIGHT_IMAGE_FLIPPED1 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped1.png'))
KNIGHT_IMAGE_FLIPPED2 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped2.png'))

global KNIGHT_IMAGE_SCALED1
KNIGHT_IMAGE_SCALED1 = pygame.transform.scale(KNIGHT_IMAGE1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHT_IMAGE_SCALED2 = pygame.transform.scale(KNIGHT_IMAGE2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHT_IMAGE_FLIPPED_SCALED1 = pygame.transform.scale(KNIGHT_IMAGE_FLIPPED1, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHT_IMAGE_FLIPPED_SCALED2 = pygame.transform.scale(KNIGHT_IMAGE_FLIPPED2, (KNIGHT_WIDTH, KNIGHT_HEIGHT))


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
global left
left = False

walkleft = [KNIGHT_IMAGE_FLIPPED_SCALED1, KNIGHT_IMAGE_FLIPPED_SCALED2]
walkright = [KNIGHT_IMAGE_SCALED1, KNIGHT_IMAGE_SCALED2]



def handle_movement(keys_pressed, knight, playerVelocityX):
    global JUMPING
    global playerPosX
    global stagePosX
    global knightPosX


    #global playerPosY

    if pygame.key.get_pressed()[pygame.K_a]:
        playerVelocityX = -5
        LEFT = True
        RIGHT = False
        #var = WIN.blit(KNIGHT_IMAGE_FLIPPED_SCALED1, (100, 100))
        #KNIGHT_IMAGE_SCALED1.fill(transparent)
        #move back a level
        #global KNIGHT_IMAGE
        #KNIGHT_IMAGE2 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped.png'))
        #knight1 = WIN.blit(KNIGHT_IMAGE2, (knight.x, knight.y))
        #if knight1:
        #    print("here3")
        #global left
        #left = True
    # LEFT
    elif pygame.key.get_pressed()[pygame.K_d]:
        playerVelocityX = 5
        LEFT = False
        RIGHT = True
        #KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'Default_Character.png'))
    #RIGHT
    if pygame.key.get_pressed()[pygame.K_SPACE] and JUMPING == False:
        JUMPING = True
        knight.y -= 150

    playerPosX += playerVelocityX

    if playerPosX > stageWidth - halfW:
         playerPosX = stageWidth - halfW
         #makes right boundary
    if playerPosX < 0:
          playerPosX = 0
          #makes left boundary
    if playerPosX < startScrollingPosX - knight.width:
          knightPosX = playerPosX
         # print("here1")
          #if the screen doesn't need to scroll then the knight can move freely
    elif playerPosX > stageWidth - startScrollingPosX:
          knightPosX = playerPosX - stageWidth + WIDTH
          #playerPosX = stageWidth + WIDTH
          #print("here12")
          #right boundary
    else:
          #playerPosX = startScrollingPosX - knight.width
          knightPosX = startScrollingPosX

          stagePosX += playerVelocityX
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
RIGHT = True
LEFT = False
def draw_window():
    #global left
    #KNIGHT_IMAGE_FLIPPED = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped.png'))
    #if left == True:
    #    WIN.blit(KNIGHT_IMAGE_FLIPPED, (100,100))

        #global KNIGHT_IMAGE
        #KNIGHT_IMAGE2 = pygame.image.load(os.path.join('Assets', 'Default_Character_Flipped.png'))
        #knight1 = WIN.blit(KNIGHT_IMAGE2, (knight.x, knight.y))
        #if knight1:
        #    print("here3")
        #global left
        #left = True
    # LEFT
        #KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'Default_Character.png'))
    #RIGHT
    global x
    global KNIGHT_IMAGE1
    global KNIGHT_IMAGE_SCALED1

    rel_x = stagePosX % BACKGROUND_IMAGE_SCALED.get_rect().width
    WIN.fill((52,192,235))
    WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width,0))
    if rel_x < WIDTH:
         WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))
    x -= 1
    pygame.draw.rect(WIN, (66,245,84), FLOOR)
    #WIN.blit(KNIGHT_IMAGE_SCALED1, (playerPosX, knight.y))
    WIN.blit(ENEMY_IMAGE_SCALED, (enemy.x, HEIGHT - FLOOR.height - ENEMY_HEIGHT))
    WIN.blit(FLOOR1_IMAGE_SCALED, (0, 130))

    #WIN.blit(KNIGHT_IMAGE_SCALED1, (100, 100))
    #WIN.blit(KNIGHT_IMAGE_SCALED2, (100, 200))
    #WIN.blit(KNIGHT_IMAGE_FLIPPED_SCALED1, (100, 300))
    #WIN.blit(KNIGHT_IMAGE_FLIPPED_SCALED2, (100, 400))
    #WIN.blit(TREE_IMAGE_SCALED, (10, FLOOR.y - 200))
    if LEFT:
        WIN.blit(walkleft[0], (playerPosX, knight.y))
    elif RIGHT:
        WIN.blit(walkright[0], (playerPosX, knight.y))

        #print("2")
    if pygame.key.get_pressed()[pygame.K_SPACE] and JUMPING == False:
        print("3")
    pygame.display.update()
if __name__ == "__main__":
    main()
