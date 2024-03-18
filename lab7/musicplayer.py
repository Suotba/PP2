import pygame
from pygame import mixer
import os

mixer.init()
pygame.init()

font = pygame.font.SysFont('Arial', 20)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Player')

pygame.mixer.music.set_endevent(pygame.USEREVENT)

def play(music_path):
    mixer.music.load(music_path)
    mixer.music.play()

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def nextm():
    global current_song_index
    if current_song_index < len(music_list) - 1:
        current_song_index += 1
    else:
        current_song_index = 0
    play(music_list[current_song_index])

def previousm():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
    else:
        current_song_index = len(music_list) - 1
    play(music_list[current_song_index])

to_path = 'MusP/Musics'
music_list = []
for file_name in os.listdir(to_path):
    music_list.append(os.path.join(to_path, file_name))

song_lengths = {}
for file_name in os.listdir(to_path):
    file_path = os.path.join(to_path, file_name)
    if file_name.endswith('.mp3'):
        sound = pygame.mixer.Sound(file_path)
        song_lengths[file_name] = sound.get_length()

current_song_index = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.USEREVENT:
            nextm()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not mixer.music.get_busy():
                if music_list:
                    play(music_list[current_song_index])
            elif event.key == pygame.K_p and mixer.music.get_pos() == -1:
                play(music_list[current_song_index])
            elif event.key == pygame.K_SPACE:
                if mixer.music.get_busy():
                    pause()
                else:
                    unpause()
            elif event.key == pygame.K_n:
                nextm()
            elif event.key == pygame.K_b:
                previousm()

    screen.fill((0, 0, 0))

    current_song = os.path.basename(music_list[current_song_index]) # Текущая песня
    song_length = song_lengths.get(current_song) # Ее длина
 
    min = pygame.mixer.music.get_pos() // 60000 # Получает время проигрываение с момента запуска песни и переводит миллисекунды в минуту
    sec = (pygame.mixer.music.get_pos() // 1000) % 60  # В секунды
    time_text = font.render(f"Time: {min:02d}:{sec:02d}", True, (255, 255, 255))
    screen.blit(time_text, (10, 40))

    # Текущая песня
    text_surface = font.render(f"Now playing: {current_song}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    # Инструкция на экране
    p_text = font.render("To start play music - P", True, (0, 255, 0))
    pause_or_unpause_text = font.render("To pause or unpause - Space", True, (192, 192, 192))
    next_text = font.render("To play next - N", True, (255, 0, 255))
    prevm_text = font.render("To play previous - B", True, (255, 255, 0))

    rect1 = p_text.get_rect(topleft=(10, 70))
    rect2 = pause_or_unpause_text.get_rect(topleft=(10, 100))
    rect4 = next_text.get_rect(topleft =(10, 130))
    rect3 = prevm_text.get_rect(topleft =(10,160))
    
    screen.blit(p_text, rect1)
    screen.blit(pause_or_unpause_text, rect2)
    screen.blit(next_text, rect3)
    screen.blit(prevm_text,rect4)

    pygame.display.flip()
    pygame.time.Clock().tick(10)

pygame.quit()
