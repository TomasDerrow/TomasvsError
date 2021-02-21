import pygame
import os
import time
#HW - Scrolling background and try to make jump more smooth using article in lesson 5 email
pygame.init()
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 5
#pygame.Surface.set_colorkey(KNIGHT_IMAGE, [255,255,255])
KNIGHT_WIDTH, KNIGHT_HEIGHT = 75, 67
knight = pygame.Rect(0, 0, KNIGHT_WIDTH, KNIGHT_HEIGHT)
KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', 'Character.png'))
KNIGHT_IMAGE_SCALED = pygame.transform.scale(KNIGHT_IMAGE, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
pygame.Surface.set_colorkey(KNIGHT_IMAGE_SCALED, [246,246,246])
BACKGROUND = pygame.image.load(os.path.join('Assets', 'Background2.png'))
BACKGROUND_IMAGE_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
FLOOR1 = pygame.image.load(os.path.join('Assets', 'Floor.png'))
FLOOR1_IMAGE_SCALED = pygame.transform.scale(FLOOR1, (900, 400))
global x
x = 0

#TREE = pygame.image.load(os.path.join('Assets', 'Tree.png'))
#TREE_IMAGE_SCALED = pygame.transform.scale(TREE, (200, 200))
global JUMPING
JUMPING = False


def handle_movement(keys_pressed, knight):
    global JUMPING
    if keys_pressed[pygame.K_a] and knight.x - vel > 0:
        knight.x -= vel
    # LEFT
    if keys_pressed[pygame.K_d]:
        knight.x += vel
    #RIGHT
    if keys_pressed[pygame.K_SPACE] and JUMPING == False:
        JUMPING = True
        knight.y -= 100
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
        handle_movement(keys_pressed, knight)
        draw_window()

    pygame.quit()

#drawing all assets
def draw_window():
    global x
    rel_x = x % BACKGROUND_IMAGE_SCALED.get_rect().width
    #WIN.fill((52,192,235))
    WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x - BACKGROUND_IMAGE_SCALED.get_rect().width,0))
    if rel_x < WIDTH:
        WIN.blit(BACKGROUND_IMAGE_SCALED, (rel_x, 0))
    x -= 1
    pygame.draw.rect(WIN, (66,245,84), FLOOR)
    WIN.blit(KNIGHT_IMAGE_SCALED, (knight.x, knight.y))
    WIN.blit(FLOOR1_IMAGE_SCALED, (0, 130))

    #WIN.blit(TREE_IMAGE_SCALED, (10, FLOOR.y - 200))
    pygame.display.update()
if __name__ == "__main__":
    main()
