import pygame
import sys

FPS = 60
WIDTH = 800
HEIGHT = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class background:
    left_side = pygame.Surface((WIDTH / 2, HEIGHT))
    right_side = pygame.Surface((WIDTH / 2, HEIGHT))
    @staticmethod
    def draw():
        background.left_side.fill((0,0,0))
        background.right_side.fill((255,255,255))
        screen.blit(background.left_side, (0,0))
        screen.blit(background.right_side, (WIDTH / 2, 0))

class ball:
    surf = pygame.Surface((20,20))
    velocity = (0,0)
    X = WIDTH / 2
    Y = HEIGHT / 2
    @staticmethod
    def process():
        ball.X += ball.velocity[0]
        ball.Y += ball.velocity[1]
        screen.blit(ball.surf, (ball.X, ball.Y))

class platforms:
    surf = pygame.Surface((20, 20))
    velocity = 10
    left_platform_y = 300
    right_platform_y = 300
    @staticmethod
    def game():
        left_platform = pygame.Surface((20, 100))
        right_platform = pygame.Surface((20, 100))
        left_platform.fill((255,255,255))
        right_platform.fill((0,0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            platforms.left_platform_y -= platforms.velocity
        if keys[pygame.K_s]:
            platforms.left_platform_y += platforms.velocity
        if keys[pygame.K_UP]:
            platforms.right_platform_y -= platforms.velocity
        if keys[pygame.K_DOWN]:
            platforms.right_platform_y += platforms.velocity
        screen.blit(left_platform, (0, platforms.left_platform_y))
        screen.blit(right_platform, (780, platforms.right_platform_y))

while True:
    background.draw()
    ball.process()
    platforms.game()

    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)