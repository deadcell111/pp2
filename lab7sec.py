import pygame
import keyboard
import os
import sys

pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 400, 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BUTTON_COLOR = (100, 100, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎵 Music Player")

font = pygame.font.Font(None, 36)

songs = [
    "songs/song_1.mp3",
    "songs/song_2.mp3",
    "songs/song_3.mp3"
]

songs = [song for song in songs if os.path.exists(song)]

if not songs:

    print("No valid songs found. Add MP3 files in the directory.")
    exit()

current_index = 0


buttons = {

    "Play": pygame.Rect(170, 130, 70, 40),
    "Stop": pygame.Rect(170, 230, 70, 40),
    "Next": pygame.Rect(90, 180, 70, 40),
    "Prev": pygame.Rect(250, 180, 70, 40)

}

def play_music():

    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()
    print(f"▶️ Playing: {songs[current_index]}")

def stop_music():

    pygame.mixer.music.stop()
    print("⏹️ Music Stopped.")

def next_song():

    global current_index
    current_index = (current_index + 1) % len(songs)
    play_music()

def previous_song():

    global current_index
    current_index = (current_index - 1) % len(songs)
    play_music()

keyboard.add_hotkey("w", play_music)
keyboard.add_hotkey("s", stop_music)
keyboard.add_hotkey("d", next_song)
keyboard.add_hotkey("a", previous_song)

print("🎵 Music Player Started! Controls:")
print("Press 'W' to Play, 'S' to Stop, 'D' for Next, 'A' for Previous")
print("Use mouse to click on buttons as well.")

running = True

while running:

    screen.fill(WHITE)

    song_text = font.render(f"Now Playing: {os.path.basename(songs[current_index])}", True, BLACK)
    screen.blit(song_text, (50, 50))

    for text, rect in buttons.items():

        pygame.draw.rect(screen, BUTTON_COLOR, rect)
        label = font.render(text, True, WHITE)
        screen.blit(label, (rect.x + 15, rect.y + 10))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            for action, rect in buttons.items():

                if rect.collidepoint(event.pos):

                    if action == "Play":

                        play_music()

                    elif action == "Stop":

                        stop_music()

                    elif action == "Next":

                        next_song()

                    elif action == "Prev":
                        
                        previous_song()

pygame.quit()
sys.exit()