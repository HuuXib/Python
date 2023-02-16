import pygame 
import os
import sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pierwsza gra klepnięta w Pythonie')


Red = (255, 0, 0)

# BORDER = pygame.rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
# VEL = 5
# BULET_VEL = 7
# MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

HIT = pygame.USEREVENT + 1

HERO_IMAGE = pygame.image.load(
    os.path.join('Assets', 'zolnierz.png'))

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'dolina.jpg')), (WIDTH, HEIGHT))

def draw_window():
        WIN.fill(Red)
        WIN.blit(BACKGROUND_IMAGE,(0, 0))
        WIN.blit(HERO_IMAGE, (p1, p2, 100, 50))
        pygame.display.update()

def main():
    Knight = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    p1=10
    p2=10
    step=5
    while run:
        sur_obj.fill(Red)
        pygame.draw.rect(sur_Red, (255,0,0), (p1, p2, 70, 65))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            p1 -= step
        if key_input[pygame.K_RIGHT]:
            p1 += step
        draw_window()
    
    pygame.quit()

if __name__=="__main__":
    main()