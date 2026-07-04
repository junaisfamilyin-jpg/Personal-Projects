import pygame
import sys

pygame.init()

name = input("Enter your name: ")

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chalk Writing Sprite")

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREY = (100, 100, 100)

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 90)

text_surface = font.render(name, True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

drawing_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)


class Chalk(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((45, 18), pygame.SRCALPHA)
        pygame.draw.rect(self.image, GREY, (0, 0, 45, 18))
        pygame.draw.rect(self.image, WHITE, (5, 4, 35, 10))
        self.rect = self.image.get_rect()
        self.rect.midleft = (text_rect.left, text_rect.centery)

    def update_position(self, x, y):
        self.rect.center = (x + 20, y)


chalk = Chalk()
sprites = pygame.sprite.Group(chalk)

x_progress = 0
writing_speed = 1

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if x_progress < text_surface.get_width():
        for y in range(text_surface.get_height()):
            colour = text_surface.get_at((int(x_progress), y))

            if colour.a > 0:
                screen_x = text_rect.left + int(x_progress)
                screen_y = text_rect.top + y
                pygame.draw.circle(drawing_surface, GREY,
                                   (screen_x, screen_y), 2)
                chalk.update_position(screen_x, screen_y)

        x_progress += writing_speed

    screen.fill(WHITE)
    screen.blit(drawing_surface, (0, 0))
    sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
