import pygame
import sys

click = 0
scr = pygame.display.set_mode((800,600))
pygame.display.set_caption("Кликер")

while True:
    scr.fill((255 ,0, 255))
    pygame.draw.circle(scr, (56,46,78), (400,300), 80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            distance_squared = (mouse_pos[0] - (400,300)[0]) ** 2 + (mouse_pos[1] - (400,300)[1]) ** 2
            if distance_squared <= 80 ** 2:
                click += 1
                print(click)
    pygame.display.update()
