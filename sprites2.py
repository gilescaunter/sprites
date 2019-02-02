import pygame
from pygame.locals import *
from car import Car
import random

pygame.init()
WHITE = (255, 255, 255)

width, height = 640, 480

screen = pygame.display.set_mode((width, height))

allSpritesList = pygame.sprite.Group()

playerCar = Car(60, 80, width, height,  5, 1)
car1 = Car(30, 80, width, height, 5, 1)


allSpritesList.add(playerCar)
allSpritesList.add(car1)


# Allowing the user to close the window...
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    for car in allSpritesList:
        car.move()
        car.bounce()
        car.repaint(WHITE)

    allSpritesList.update()

    screen.fill(WHITE)


    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    allSpritesList.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()