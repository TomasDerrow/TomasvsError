import pygame
import os
#remove white parts with photoshop
pygame.init()
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Tomas vs Error")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FLOOR = pygame.Rect(0, HEIGHT-50, WIDTH, 50)
vel = 3
#pygame.Surface.set_colorkey(KNIGHT_IMAGE, [255,255,255])
KNIGHT_WIDTH, KNIGHT_HEIGHT = 128, 80
knight = pygame.Rect(0, 0, KNIGHT_WIDTH, KNIGHT_HEIGHT)
KNIGHT_IMAGE = pygame.image.load(os.path.join('Assets', '375-3751215_small-armor-knight-pixel-art-knight.png'))
KNIGHT_IMAGE_SCALED = pygame.transform.scale(KNIGHT_IMAGE, (KNIGHT_WIDTH, KNIGHT_HEIGHT))
pygame.Surface.set_colorkey(KNIGHT_IMAGE_SCALED, [246,246,246])

def handle_movement(keys_pressed, knight):
    if keys_pressed[pygame.K_a] and knight.x - vel > 0:
        knight.x -= vel
    # LEFT
    if keys_pressed[pygame.K_d]:
        knight.x += vel
    #RIGHT
    if keys_pressed[pygame.K_SPACE]:
        knight.y -= 15





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
        if knight.y < HEIGHT - FLOOR.height - KNIGHT_HEIGHT:
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
    WIN.fill((52,192,235))
    pygame.draw.rect(WIN, (66,245,84), FLOOR)
    WIN.blit(KNIGHT_IMAGE_SCALED, (knight.x, knight.y))
    pygame.display.update()
if __name__ == "__main__":
    main()
