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

#Game Window
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

#Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    display = myFont.render('Game Over!, Try Again ?', True, red)
    displayRect = display.get_rect()
    displayRect.midtop = (350, 15)
    playSurface.blit(display,displayRect)
    pygame.display.flip()   # flip = update
    time.sleep(4)
    pygame.quit()
    sys.exit()

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
                pygame.event.post(pygame.eventevent(QUIT))

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
    if direction == 'LEDT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #Snake body
    snakeBody.insert(0, list(snakePos))
    #Match snake head to foodPos
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        isFood = False  #make spawn food into a function ?
    else:
        snakeBody.pop()
    #Spawn food if none
    if isFood == False:
        foodPos
    isFood = True

    #white bg
    playSurface.fill(white)
    pygame.display.flip()
