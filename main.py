import sys
import random
import time
import pygame
from pygame.locals import *

pygame.init()

# Colors

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# window info
screen_width = 300
screen_height = 300
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Bird Spike")

# Frames per second
FPS = 60
FramePerSec = pygame.time.Clock()


class Spike(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("spike.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bird.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
S1 = Spike()
# Game loop starts
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    S1.update()

    DISPLAYSURF.fill(white)
    P1.draw(DISPLAYSURF)
    S1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)