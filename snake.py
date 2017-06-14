#Game Imports
import pygame
import sys
import random
import time

#Compiler test
init_debug = pygame.init()
if init_debug[1] > 0:
    print("{0} errors occured, sys shut down...".format(init_debug[1]))
    sys.exit(-1)
else:
    print("pyagem compiled Successfully")


#Colors used
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

#Global variables
#Screen resolution
playSurface = pygame.display.set_mode((720, 460))

#Window name
pygame.display.set_caption('Snake!')

#FPS
fpsController = pygame.time.Clock()

#Snake
snakePos = [100,50] # starting position
snakeBody = [[100,50],[90,50],[80,50]] # snake body spawn

#spawn food based on screen resolution height (720) width (460) * 10
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
isFood = True   #food spawn check

#Directions
direction = 'RIGHT'
changeto = direction

#Score
score = 0

#Game over function
def GameOver():
    font1 = pygame.font.SysFont('monaco', 72)
    display = font1.render('Game Over!, Try Again ?', True, red)
    displayRect = display.get_rect()
    displayRect.midtop = (350, 15)
    playSurface.blit(display,displayRect)
    pygame.display.flip()   # flip = update
    Score(0)
    time.sleep(4)
    pygame.quit()
    sys.exit()

#Show score on screen
def Score(scorePos=1):
    scoreFont = pygame.font.SysFont('monaco', 24)
    scoreDispaly = scoreFont.render('Score: {0}'.format(score), True, blue)
    scoreRect = scoreDispaly.get_rect()
    #position of score after game over
    if scorePos == 1:
        scoreRect.midtop = (80, 10)
    else:
        scoreRect.midtop = (360, 120)
    playSurface.blit(scoreDispaly,scoreRect)

#Program flow
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.eventevent(pygame.QUIT))

    #No direction backtracking
    if changeto == 'RIGHT' and not direction == 'LEFT' :
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT' :
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN' :
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP' :
        direction = 'DOWN'

    #Snake movement
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #Snake body
    snakeBody.insert(0, list(snakePos))
    #Match snake head to foodPos
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        isFood = False
    else:
        snakeBody.pop()
    #Spawn food if none
    if isFood == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    isFood = True

    #White bg
    playSurface.fill(white)
    #Draw snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))
    #Draw food
    pygame.draw.rect(playSurface, black, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    #Screen boundary & game over condition
    if snakePos[0] > 710 or snakePos[0] < 0:
        GameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        GameOver()
    #Snake eat self
    for block in snakeBody[1:]: #start from index 1 of list
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            GameOver()

    #draw game assets
    pygame.display.flip()
    Score()
    fpsController.tick(30)  #run at 30fps
