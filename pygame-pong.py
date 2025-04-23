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
# Default values
ball_moving = True
sound_on = True
difficulty = "normal"
player_speed = 7
player_color = (GREEN)
opponent_speed = 5
if difficulty == "easy":
    opponent_speed = 3
elif difficulty == "hard":
    opponent_speed = 7
else:
    opponent_speed = 5  # normal
opponent_color = (RED)
ball_speed_x = 5
ball_speed_y = 5
ball_color = (WHITE)
ball_touched_paddle = False
win_played = False
player_score = 0
opponent_score = 0
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
# Read settings from settings.txt
try:
    settings_file = open("settings.txt", "r")
    lines = settings_file.readlines()
    for line in lines:
        if "sound=" in line:
            value = line.strip().split("=")[1]
            if value == "False":
                sound_on = False
        elif "difficulty=" in line:
            difficulty = line.strip().split("=")[1]
    settings_file.close()
except:
    pass  # use default if file not found

# ----------- SOUND SETUP -----------
# Load sound files from assets/sounds
bounce_sound = pygame.mixer.Sound("assets/Sounds/ball_sound.wav")  # Paddle hit sound
win_sound = pygame.mixer.Sound("assets/Sounds/Win_sound.wav")  # Victory sound
pygame.mixer.music.load("assets/Sounds/Background.wav")  # Background music

# Set sound volumes (optional)
bounce_sound.set_volume(0.8)  # 80% volume
win_sound.set_volume(1.0)     # Full volume
if not sound_on:
    bounce_sound.set_volume(0)
    win_sound.set_volume(0)
    pygame.mixer.music.set_volume(0)

# Loop background music indefinitely
pygame.mixer.music.play(-1)

# ----------- IMAGE ASSETS -----------
# Load splash screen image
welcome_img = pygame.image.load("Assets/Images/welcome.png")
credits_img = pygame.image.load("Assets/Images/credits.png")
credits_img = pygame.transform.scale(credits_img, (WIDTH, HEIGHT))


# ----------- DRAW FUNCTIONS -----------
font = pygame.font.SysFont(None, 36)

# Start screen function
def show_start_screen():
    waiting = True
    font = pygame.font.SysFont(None, 48)
    title_text = font.render("Welcome to Pong!", True, WHITE)
    start_text = font.render("Press SPACE to Start", True, WHITE)
    toggle_text = font.render("Press T to Toggle Sound | D to Change Difficulty", True, WHITE)


    while waiting:
        screen.fill(BLACK)

        # draw the splash image centered
        screen.blit(welcome_img, (WIDTH // 2 - welcome_img.get_width() // 2, HEIGHT // 2 - welcome_img.get_height() // 2 - 50))

        # draw text below it
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT - 150))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT - 100))
        screen.blit(toggle_text, (WIDTH // 2 - toggle_text.get_width() // 2, HEIGHT - 60))


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    waiting = False


# Function to blit all surfaces to the screen
def draw_objects():
    screen.fill(BLACK)
    screen.blit(paddle_surface, player_rect)
    screen.blit(opponent_surface, opponent_rect)
    screen.blit(ball_surface, ball_rect)
    screen.blit(midline_surface, midline_rect)
    # Draw player score (left, green)
    player_text = font.render(f"Player: {player_score}", True, GREEN)
    screen.blit(player_text, (20, 20))

    # Draw opponent score (right, red)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, RED)
    screen.blit(opponent_text, (WIDTH - opponent_text.get_width() - 20, 20))
    
    # Draw settings text    
    settings_text = font.render("T: Toggle Sound | D: Change Difficulty", True, WHITE)
    screen.blit(settings_text, (WIDTH // 2 - settings_text.get_width() // 2, 60))


# End screen function
def show_end_screen(message):
    global player_score, opponent_score

    # Write the result to the log file  
    log_file = open("log.txt", "a")
    log_file.write("Result: " + message + ", Player Score: " + str(player_score) + ", Opponent Score: " + str(opponent_score) + "\n")
    log_file.close()

    font = pygame.font.SysFont(None, 48)
    end_text = font.render(message, True, WHITE)
    restart_text = font.render("Press R to Restart or ESC to Quit", True, WHITE)

    waiting = True

    while waiting:
        screen.blit(credits_img, (0, 0))  # Show the credits image as background

        # Draw a black rectangle to cover the credits image
        pygame.draw.rect(screen, BLACK, (0, 20, WIDTH, 100))

        # Overlay messages moved text higher up
        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, 30))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 80))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    waiting = False  # Go back to game
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Countdown function
def countdown():
    global ball_moving
    ball_moving = False
    font = pygame.font.SysFont(None, 72)

    for i in range(3, 0, -1):
        screen.fill(BLACK)
        draw_objects()

        # Draw a rect behind the countdown text
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)  
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        # Display countdown number
        countdown_text = font.render(str(i), True, WHITE)
        screen.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2 - countdown_text.get_height() // 2))
        pygame.display.flip()

        # Wait 1 second (1000 ms) WITHOUT freezing game loop
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 1000:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    ball_moving = True

# ----------- MAIN LOOP -----------
show_start_screen()

running = True

while running:
    # event handling for quitting the game
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == KEYDOWN:
            # Toggle sound with T
            if event.key == K_t:
                sound_on = not sound_on

                if sound_on:
                    bounce_sound.set_volume(0.8)
                    win_sound.set_volume(1.0)
                    pygame.mixer.music.set_volume(0.5)
                else:
                    bounce_sound.set_volume(0)
                    win_sound.set_volume(0)
                    pygame.mixer.music.set_volume(0)

                # Save to settings.txt
                settings_file = open("settings.txt", "w")
                settings_file.write("sound=" + str(sound_on) + "\n")
                settings_file.write("difficulty=" + difficulty + "\n")
                settings_file.close()

            # Toggle difficulty with D
            elif event.key == K_d:
                if difficulty == "easy":
                    difficulty = "normal"
                    opponent_speed = 5
                elif difficulty == "normal":
                    difficulty = "hard"
                    opponent_speed = 7
                else:
                    difficulty = "easy"
                    opponent_speed = 3

                # Save to settings.txt
                settings_file = open("settings.txt", "w")
                settings_file.write("sound=" + str(sound_on) + "\n")
                settings_file.write("difficulty=" + difficulty + "\n")
                settings_file.close()

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
    if ball_moving:
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

    # scoring logic
    if ball_rect.left <= 0:
        opponent_score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1
        countdown()

    elif ball_rect.right >= WIDTH:
        player_score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1
        countdown()

    # win or lose condition
    if player_score >= 5 and not win_played: # Changed from 10 to 5
        win_sound.play()
        win_played = True
        show_end_screen("You Win!")

        # Update score file
        file = open("score.txt", "w")
        file.write("Player Wins: 1\n")
        file.write("Opponent Wins: 0\n")
        file.close()

        # Reset game state
        player_score = 0
        opponent_score = 0
        win_played = False
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        #should reset the paddle to center
        player_rect.centery = HEIGHT //2
        opponent_rect.centery = HEIGHT //2

    elif opponent_score >= 5 and not win_played: # Changed from 10 to 5
        win_played = True
        show_end_screen("You Lose!")

        # Update score file
        file = open("score.txt", "w")
        file.write("Player Wins: 0\n")
        file.write("Opponent Wins: 1\n")
        file.close()

        # Reset game state
        player_score = 0
        opponent_score = 0
        win_played = False
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        #should reset the paddle to center
        player_rect.centery = HEIGHT //2
        opponent_rect.centery = HEIGHT //2

    # drawing the game objects
    draw_objects()    

    # updating the display
    pygame.display.flip()
    clock.tick(60)

# ----------- CLEANUP -----------
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
sys.exit()
