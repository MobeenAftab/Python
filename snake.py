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
    pygame.display.flip()

gameOver()
time.sleep(10)
