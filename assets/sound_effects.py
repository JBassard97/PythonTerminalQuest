import pygame
import threading

pygame.mixer.init()


def play_async_audio(event: str):
    if event == "accept":
        sound_file = "assets/sounds/pokemon_a_press.mp3"
    if event == "decline":
        sound_file = "assets/sounds/pokemon_wall_bump.mp3"
    else:
        raise ValueError("That is not a valid event string")

    sound = pygame.mixer.Sound(sound_file)
    sound_thread = threading.Thread(target=sound.play, daemon=True)
    sound_thread.start()
