
import pygame

pygame.init()
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
BLACK = (0,0,0)
ORANGE=(255,165,0)
VIOLET=(127,0,255)
CIRCLE_CENTER = [WIDTH/2,HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS=5
ball_pos=[WIDTH/2,HEIGHT/2-120]
running = True

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
            
    window.fill(BLACK)
    pygame.draw.circle(window,ORANGE,CIRCLE_CENTER,CIRCLE_RADIUS,3)
    pygame.draw.circle(window,VIOLET,ball_pos,BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()