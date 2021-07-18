import pygame
import os
import time

'''
HOMEWORK SECTION
* work on enemy range
'''

# Screen Settings
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

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
        self.enemy_left = True
        self.enemy_right = False

        Character.__init__(self)


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
    'Assets', 'Default_Character_Block1.png', player.knight_width, player.knight_height)

knightSwing1_left = player.loadImage(
    'Assets', 'Default_Character_Swing_Flipped1.png', player.knight_width, player.knight_height)
knightSwing2_left = player.loadImage(
    'Assets', 'Default_Character_Swing_Flipped2.png', player.knight_width, player.knight_height)
knightSwing3_left = player.loadImage(
    'Assets', 'Default_Character_Swing_Flipped3.png', player.knight_width, player.knight_height)

knightBlock1_left = player.loadImage(
    'Assets', 'Default_Character_Block_Flipped1.png', player.knight_width, player.knight_height)

enemy1_right = enemy.loadImage('Assets', 'enemy.png', 100, 100)

# Rectangles defined
'''
TODO: Can be defined in our loadImage method, may need to change though
'''
knightRect = pygame.Rect(player.knightPosX, 0,
                         player.knight_width, player.knight_height)
knight = pygame.Rect(WIDTH/2 - player.knight_width, 450-player.knight_height,
                     player.knight_width, player.knight_height)

enemyKnight = pygame.Rect(WIDTH/2 - enemy.enemy_width, HEIGHT-FLOOR.height -
                          enemy.enemy_height, enemy.enemy_width, enemy.enemy_height)


enemyRange = pygame.Rect(enemyKnight.x, enemyKnight.y, 500, 200)


Character_Movements = [
    pygame.image.load(os.path.join('Assets', 'Default_Character1N.png')),
    pygame.image.load(os.path.join(
        'Assets', 'Default_Character_Flipped1.png')),
    pygame.image.load(os.path.join('Assets', 'Default_Character2.png'))]


# Lists defined
walkLeft = [knight1_left, knight2_left, knight3_left, knight4_left]
walkRight = [knight1_right, knight2_right, knight3_right, knight4_right]

swingLeft = [knightSwing1_left, knightSwing2_left, knightSwing3_left]
swingRight = [knightSwing1_right, knightSwing2_right, knightSwing3_right]

# functions


def handle_movement(keys_pressed, knight):
    '''
    TODO: Add comments near if statements describing what is happening
    '''

    if pygame.key.get_pressed()[pygame.K_a]:
        player.velocity = -5
        player.left = True
        player.right = False
        player.still = False
    #if press a move left
    elif pygame.key.get_pressed()[pygame.K_d]:
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
        print("jump2")
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
        # if the screen doesn't need to scroll then the knight can move freely
    elif player.playerPosX > stageWidth - startScrollingPosX:
        player.knightPosX = player.playerPosX - stageWidth + WIDTH - knight.width
        #playerPosX = stageWidth + WIDTH
        # right boundary
    else:
        #playerPosX = startScrollingPosX - knight.width
        player.knightPosX = startScrollingPosX - knight.width
        player.stagePosX += player.velocity

    player.knightrect = pygame.Rect(
        player.knightPosX, knight.y, player.knight_width, player.knight_height)

def moveAutomatically(b_range, e_range, velocity = 2):

    if player.knightPosX + knight.width > b_range and player.knightPosX < e_range:
        if player.knightPosX > enemyKnight.x:
            enemyKnight.x += velocity
        elif player.knightPosX < enemyKnight.x:
            enemyKnight.x -= velocity
    else:
        if enemy.enemy_left:
            print("1")
            if enemyKnight.x < 0:
                print("2")
                enemy.enemy_right = True
                enemy.enemy_left = False
            enemyKnight.x -= velocity
        elif enemy.enemy_right:
            print("3")
            if enemyKnight.x > WIDTH - enemy.enemy_width:
                enemy.enemy_left = True
                enemy.enemy_right = False
            enemyKnight.x += velocity


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
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
        draw_window()
        handle_movement(keys_pressed, knight)
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
    global x

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

    WIN.blit(FLOOR1_IMAGE_SCALED,
             (rel_x - FLOOR1_IMAGE_SCALED.get_rect().width, 130))
    if rel_x < WIDTH:
        WIN.blit(FLOOR1_IMAGE_SCALED, (rel_x, 130))

    '''
    TODO: Create a separate function that displays text
    something like
    i.e. def renderText(text, posX, posY)
    '''

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    #positions = myfont.render("Playerposx: " + str(playerPosX) + " knightposx: " + str(knightPosX) + "stagePosX" + str(stagePosX), False, (0, 0, 0))
    # WIN.blit(positions,(0,100))
    healthtext = myfont.render(str(enemyKnight.x), False, (0, 0, 0))
    WIN.blit(healthtext, (200,20))
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

    '''
    TODO: don't need the alive attribute,
        check if health is <= 0
        also this check should be in the handle_damage function
    '''
    if player.health <= 0:
        pygame.draw.rect(WIN, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        WIN.blit(deathtext, (WIDTH/2 - text_width/2, HEIGHT/2 - text_height/2))



if __name__ == "__main__":
    main()
