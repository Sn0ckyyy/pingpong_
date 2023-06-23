import pygame
import sys

pygame.init()
BLUE = (50, 88, 168)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)

posX_block2 = 150
posY_block2 = 150
posY_block1 = 150
posX_circle = 80
posY_circle = 150
circle_right = True
circle_top = True

f1 = pygame.font.Font(None, 36)
score_p1 = f1.render('0', 1, (180, 0, 0))
score_p2 = f1.render('0', 1, (180, 0, 0))

speed = 6
WIDTH = 800
HEIGHT = 400
 
ball_texture = pygame.image.load('tenis_ball.png')
pads = pygame.image.load('racket.png')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    screen.fill(BLUE)
    screen.blit(score_p1, (10, 50))
    screen.blit(score_p2, (770, 50))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        if posY_block2 > 0:
            posY_block2 -= speed
    if pressed_keys[pygame.K_DOWN]:
        if posY_block2 + 100 < HEIGHT:
            posY_block2 += speed
    if pressed_keys[pygame.K_w]:
        if posY_block1 > 0:
            posY_block1 -= speed
    if pressed_keys[pygame.K_s]:
        if posY_block1 + 100 < HEIGHT:
            posY_block1 += speed
    if posX_circle - 25 <= 0:
        circle_right = True
 
    if posY_circle - 25 <= 0:
        circle_top = False
    elif posY_circle + 25 >= HEIGHT:
        circle_top = True
    if circle_right:
        posX_circle += speed
    else:
        posX_circle -= speed
    if circle_top:
        posY_circle -= speed
    else:
        posY_circle += speed
    if posY_block1 <= posY_circle <= posY_block1 + 50 and WIDTH - 10 <= posX_circle + 25 <= WIDTH:
        circle_right = False
    if posY_block2 <= posY_circle <= posY_block2 + 50 and WIDTH - 10 <= posX_circle + 25 <= WIDTH:
        circle_right = False
    elif posX_circle + 25 > WIDTH:
        pygame.quit() 
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, pads, (0, posY_block1, 20, 100))
    pygame.draw.rect(screen, pads, (780, posY_block2, 20, 100))
    pygame.draw.circle(screen, ball_texture, (posX_circle, posY_circle), 25)
    pygame.display.update()
