import pygame 
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pierwsza gra klepnięta w Pythonie')


Red = (255, 0, 0)

# BORDER = pygame.rect(WIDTH//2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
BULET_VEL = 7
MAX_BULLETS = 3
SACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

HIT = pygame.USEREVENT + 1

HERO_IMAGE = pygame.image.load(
    os.path.join('Assets', 'zolnierz.png'))

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def draw_window():
    WIN.fill(BACKGROUND_IMAGE)
    WIN.blit(HERO_IMAGE)
    pygame.display.update()

def main():

