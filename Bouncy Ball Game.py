import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Bouncy Ball Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 80, 255)
RED = (255, 50, 50)

COLORS = [
    (255, 50, 50),    # Red
    (0, 80, 255),     # Blue
    (0, 200, 80),     # Green
    (255, 200, 0),    # Yellow
    (180, 0, 255),    # Purple
    (255, 120, 0),    # Orange
    (0, 200, 255)     # Cyan
]

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

paddle = pygame.Rect(30, HEIGHT // 2 - 60, 20, 120)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 25, 25)

paddle_speed = 7
ball_speed_x = 5
ball_speed_y = 5

score = 0
game_over = False

ball_color = RED
paddle_color = BLUE


def random_color(current_color):
    new_color = random.choice(COLORS)

    while new_color == current_color:
        new_color = random.choice(COLORS)

    return new_color


def reset_ball():
    global ball_speed_x, ball_speed_y, ball_color, paddle_color

    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = random.choice([-5, 5])
    ball_speed_y = random.choice([-5, 5])

    ball_color = RED
    paddle_color = BLUE


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                paddle.y = HEIGHT // 2 - 60
                reset_ball()

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_UP]:
            paddle.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            paddle.y += paddle_speed

        if paddle.top < 0:
            paddle.top = 0
        if paddle.bottom > HEIGHT:
            paddle.bottom = HEIGHT

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0:
            ball.top = 0
            ball_speed_y *= -1
            ball_color = random_color(ball_color)

        if ball.bottom >= HEIGHT:
            ball.bottom = HEIGHT
            ball_speed_y *= -1
            ball_color = random_color(ball_color)

        if ball.right >= WIDTH:
            ball.right = WIDTH
            ball_speed_x *= -1
            ball_color = random_color(ball_color)

        if ball.colliderect(paddle):
            ball.left = paddle.right
            ball_speed_x *= -1

            ball_color = random_color(ball_color)
            paddle_color = random_color(paddle_color)

            score += 1

        if ball.left <= 0:
            game_over = True

    screen.fill(WHITE)

    pygame.draw.rect(screen, paddle_color, paddle)
    pygame.draw.ellipse(screen, ball_color, ball)

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))

    if game_over:
        over_text = font.render("Game Over", True, BLACK)
        restart_text = font.render("Press SPACE to restart", True, BLACK)

        screen.blit(over_text, over_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 30)))
        screen.blit(restart_text, restart_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()

pygame.quit()
sys.exit()
