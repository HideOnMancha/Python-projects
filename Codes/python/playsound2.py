import pygame
import sys
import pyautogui as p 

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 350))
pygame.display.set_caption("Music Player")

# Load the music file
# Make sure to replace 'your_music_file.mp3' with the path to your music file
pygame.mixer.music.load('C:/Users/Luan/Downloads/mcrafadavj.mp3') 

volume = 0.5  # Set initial volume to 50%
pygame.mixer.music.set_volume(volume)

# Function to play music
def play_music():
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Function to increase volume
def increase_volume():
    global volume
    volume = min(volume + 0.1, 1.0)  # Increase volume by 10%, max 1.0
    pygame.mixer.music.set_volume(volume)

# Function to decrease volume
def decrease_volume():
    global volume
    volume = max(volume - 0.1, 0.0)  # Decrease volume by 10%, min 0.0
    pygame.mixer.music.set_volume(volume)

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Main loop
running = True
playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Press 'P' to play music
                if not playing:
                    play_music()
                    playing = True
            elif event.key == pygame.K_s:  # Press 'S' to stop music
                if playing:
                    stop_music()
                    playing = False

    # Fill the screen with a color
    screen.fill((255, 255, 255))
    
    # Display instructions
    font = pygame.font.Font(None, 36)
    text = font.render("Press 'P' to Play, 'S' to Stop", True, (0, 0, 0))
    screen.blit(text, (100, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()