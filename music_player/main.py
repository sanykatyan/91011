import pygame
import os
import sys

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 30)


music_dir = "music"
songs = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]

if not songs:
    print("Нет треков в папке music 💀")
    sys.exit()

index = 0
playing = False

def load_and_play():
    global playing
    path = os.path.join(music_dir, songs[index])
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    playing = True

clock = pygame.time.Clock()

while True:
    screen.fill((20, 20, 20))

    
    track_text = font.render(f"Track: {songs[index]}", True, (255, 255, 255))
    controls_text = font.render("P-play/pause S-stop N-next B-back Q-quit", True, (200, 200, 200))

    screen.blit(track_text, (20, 60))
    screen.blit(controls_text, (20, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                if not playing:
                    load_and_play()
                else:
                    pygame.mixer.music.pause()
                    playing = False

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False

            if event.key == pygame.K_n:
                index = (index + 1) % len(songs)
                load_and_play()

            if event.key == pygame.K_b:
                index = (index - 1) % len(songs)
                load_and_play()

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    clock.tick(60)