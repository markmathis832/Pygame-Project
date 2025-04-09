
# CSE 1321 Pong - Project Outline

# ----------- IMPORTS -----------
import pygame
import sys
from pygame.locals import *
from datetime import datetime

# ----------- INITIAL SETUP -----------
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CSE 1321 Pong Pygame Project")
clock = pygame.time.Clock()

# ----------- COLORS -----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ----------- VARIABLES -----------
player_speed = 7
opponent_speed = 5
ball_speed_x = 5
ball_speed_y = 5
score = 0
result = ""

# ----------- SURFACES -----------
# Define all 10 required visible Surface objects:
# 1. Display surface (screen)
# 2-3. Paddles (player and opponent)
# 4. Ball
# 5. Midline
# 6. Instructions surface
# 7. Score display surface
# 8. Win text surface
# 9. Lose text surface
# 10. Restart/Quit button surfaces

# ----------- RECT OBJECTS -----------
# Define pygame.Rects for paddles, ball, and buttons

# ----------- FILE IO -----------
# Read from files:
# - instructions.txt (game instructions)
# - config.txt (initial settings)
# Write to files:
# - score.txt (track high scores)
# - log.txt (log win/lose states)
# - settings.txt (save user preferences)

# ----------- SOUND SETUP -----------
# Load at least 2 sound files
# - bounce.wav
# - win.wav or lose.wav

# ----------- DRAW FUNCTION -----------
# Function to blit all surfaces to the screen
# - Blit paddles, ball, UI elements, and buttons

# ----------- INPUT HANDLING -----------
# Process keyboard input (W/S, arrow keys, Esc, R)
# Process mouse input if needed (for restart/quit)

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
# Main game loop to handle:
# - Input
# - Movement
# - Drawing
# - State updates

# ----------- END GAME / RESTART LOGIC -----------
# Show end screen with win/lose
# Allow restart or quit using keys or buttons

# ----------- CLEANUP -----------
# Quit pygame and clean up resources
