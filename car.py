import pygame
#import spritesheet
import math

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, x, y, width, height, speed, angle):
        # Call the parent class (Sprite) constructor
        super(Car, self).__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([x, y])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the car.
        self.width = width
        self.height = height
        self.speed = speed
        self.angle = angle
        self.x = x
        self.y = y
        self.size = 20

        self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += math.sin(self.angle) * self.speed
        self.rect.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        if self.rect.x > self.width - self.size:
            self.rect.x = 2 * (self.width - self.size) - self.rect.x
            self.angle = - self.angle

        elif self.rect.x < self.size:
            self.rect.x = 2 * self.size - self.rect.x
            self.angle = - self.angle

        if self.rect.y > self.height - self.size:
            self.rect.y = 2 * (self.height - self.size) - self.rect.y
            self.angle = math.pi - self.angle

        elif self.rect.y < self.size:
            self.rect.y = 2 * self.size - self.rect.y
            self.angle = math.pi - self.angle


    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, WHITE, self.rect)
