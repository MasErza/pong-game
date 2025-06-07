import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ukuran objek
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 20

# Kecepatan
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Pemain
player1 = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Skor
score1, score2 = 0, 0
font = pygame.font.SysFont(None, 48)

# Loop utama
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # FPS

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gerakan pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Gerakan bola
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Tabrakan dengan dinding
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Tabrakan dengan paddle
    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_SPEED_X *= -1

    # Skor
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        BALL_SPEED_X *= -1
    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        BALL_SPEED_X *= -1

    # Gambar
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, player1)
    pygame.draw.rect(SCREEN, WHITE, player2)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    score_text = font.render(f"{score1}   {score2}", True, WHITE)
    SCREEN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()