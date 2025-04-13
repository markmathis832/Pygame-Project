
# CSE 1321 Pong - Project Outline

# ----------- IMPORTS -----------
import pygame
import sys
from pygame.locals import *
from datetime import datetime

# ----------- INITIAL SETUP -----------
pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("CSE 1321 Pong Pygame Project")

clock = pygame.time.Clock()

# ----------- COLORS -----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# ----------- VARIABLES -----------
player_speed = 7
player_color = (GREEN)
opponent_speed = 5
opponent_color = (RED)
ball_speed_x = 5
ball_speed_y = 5
ball_color = (WHITE)
ball_touched_paddle = False
win_played = False
score = 0
result = ""

# ----------- SURFACES -----------
# 1. Display surface (screen)
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# 2-3. Paddles (player and opponent)
paddle_surface = pygame.Surface((10, 100))
paddle_surface.fill(player_color)
opponent_surface = pygame.Surface((10, 100))
opponent_surface.fill(opponent_color)

# 4. Ball
ball_surface = pygame.Surface((20, 20))
ball_surface.fill(ball_color)

# 5. Midline
midline_surface = pygame.Surface((2, HEIGHT))
midline_surface.fill(WHITE)

# 6. Instructions surface
instructions_surface = pygame.Surface((WIDTH, 100))
instructions_surface.fill(WHITE)

# 7. Score display surface
score_surface = pygame.Surface((100, 50))
score_surface.fill(WHITE)

# 8. Win text surface
win_surface = pygame.Surface((WIDTH, HEIGHT))
win_surface.fill(WHITE)

# 9. Lose text surface
lose_surface = pygame.Surface((WIDTH, HEIGHT))
lose_surface.fill(WHITE)

# 10. Restart/Quit button surfaces
restart_surface = pygame.Surface((100, 50))
restart_surface.fill(WHITE)

# ----------- RECT OBJECTS -----------
# Define pygame.Rects for paddles, ball, and buttons

# 1-2. Paddles (player and opponent)
player_rect = paddle_surface.get_rect(midleft=(20, HEIGHT / 2))
opponent_rect = opponent_surface.get_rect(midright=(WIDTH - 20, HEIGHT / 2))

# 3. Ball
ball_rect = ball_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# 4. Midline
midline_rect = midline_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# 5. Instructions surface
instructions_rect = instructions_surface.get_rect(center=(WIDTH / 2, 50))

# 6. Score display surface
score_rect = score_surface.get_rect(center=(WIDTH / 2, 100))

# 7. Win text surface
win_rect = win_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# 8. Lose text surface
lose_rect = lose_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# 9. Restart/Quit button surfaces
restart_rect = restart_surface.get_rect(center=(WIDTH / 2, HEIGHT - 50))


# ----------- FILE IO -----------
# Read from files:
# - instructions.txt (game instructions)
# - config.txt (initial settings)
# Write to files:
# - score.txt (track high scores)
# - log.txt (log win/lose states)
# - settings.txt (save user preferences)

# ----------- SOUND SETUP -----------
# Load sound files from assets/sounds
bounce_sound = pygame.mixer.Sound("assets/Sounds/ball_sound.wav")  # Paddle hit sound
win_sound = pygame.mixer.Sound("assets/Sounds/Win_sound.wav")  # Victory sound
pygame.mixer.music.load("assets/Sounds/Background.wav")  # Background music

# Set sound volumes (optional)
bounce_sound.set_volume(0.8)  # 80% volume
win_sound.set_volume(1.0)     # Full volume

# Loop background music indefinitely
pygame.mixer.music.play(-1)

# ----------- DRAW FUNCTION -----------
# Function to blit all surfaces to the screen
def draw_objects():
    screen.fill(BLACK)
    screen.blit(paddle_surface, player_rect)
    screen.blit(opponent_surface, opponent_rect)
    screen.blit(ball_surface, ball_rect)
    screen.blit(midline_surface, midline_rect)
    # screen.blit(score_surface, score_rect)
    # screen.blit(instructions_surface, instructions_rect)
    # Optional: draw restart/quit buttons later

# ----------- MOVEMENT FUNCTIONS -----------
# Move player paddle based on key input
# Move opponent paddle (AI or fixed speed)
# Move ball, bounce off edges and paddles

# ----------- COLLISION DETECTION -----------
# Detect ball collision with paddles and walls

# ----------- GAME LOGIC -----------
# Check for win/lose conditions
# Trigger end screen and file writing


# ----------- MAIN LOOP -----------
running = True

while running:
    # event handling for quitting the game
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    # player paddle movement
    keys = pygame.key.get_pressed()
    if keys[K_w] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[K_s] and player_rect.bottom < HEIGHT:
        player_rect.y += player_speed

    # opponent bot movement
    if opponent_rect.top < ball_rect.y:
        opponent_rect.y += opponent_speed
    if opponent_rect.bottom > ball_rect.y:
        opponent_rect.y -= opponent_speed

    # ball movement
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # ball collision with walls
    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_speed_y *= -1

    # ball collision with paddles
    if ball_rect.colliderect(player_rect) or ball_rect.colliderect(opponent_rect):
        if not ball_touched_paddle:
            ball_speed_x *= -1
            ball_touched_paddle = True
            bounce_sound.play()
        else:
            ball_touched_paddle = False 

    # scoring when ball goes off screen
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # win sound when a player wins
    if score >= 10 and not win_played:  # Assuming score of 10 is a win condition
        win_sound.play()
        win_played = True

    # drawing the game objects
    draw_objects()    

    # updating the display
    pygame.display.flip()
    clock.tick(60)

# ----------- END GAME / RESTART LOGIC -----------
# Show end screen with win/lose
# Allow restart or quit using keys or buttons

# ----------- CLEANUP -----------
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
sys.exit()