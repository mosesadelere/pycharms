import pygame
from pygame.locals import *
from random import *



pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Ping Pong Game')

paddleA_col = (0,0,255)
paddleB_col = (255,0,0)
ball_col = (0,255,0)
xA, yA = 0, 275
xB, yB = 790, 275
xBall, yBall = 400, 300
ball_radius = 10
width, length = 10, 50
dx = 10
dy = 10

running = True
while running == True:
    padA = pygame.Rect(xA, yA, width, length)
    padB = pygame.Rect(xB, yB, width, length)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, paddleA_col, padA)
    pygame.draw.rect(screen, paddleB_col, padB)
    pygame.draw.circle(screen, ball_col, (xBall, yBall), ball_radius)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_r:
                yA -= 20
            elif event.key == K_w:
                yA += 20
            elif event.key == K_l:
                yB += 20
            elif event.key == K_m:
                yB -= 20

    xBall += 1
    yBall += 1
    if yBall == 10 and (xBall >= 10 or xBall < 800):
        yBall += 1
        xBall += 1
    elif yBall <= 599 and (xBall >= 10 or xBall < 800):
        yBall -= 1
        xBall -= 1
    elif xBall == 10 and (yBall >= 10 or yBall < 599):
        pass
    #xBall += 1
    #yBall += 1

    pressedKey = pygame.key.get_pressed()

    #if pressedKey[pygame.K_SPACE]:
     #   yA += 5


    #screen.fill((0,0,0))

    #pygame.display.flip()
    pygame.display.update()


