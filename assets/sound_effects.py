import pygame
import threading

pygame.mixer.init()


def play_async_audio(event: str):
    valid_params = ["accept", "decline"]

    if event == "accept":
        sound_file = "assets/sounds/pokemon_a_press.mp3"
    if event == "decline":
        sound_file = "assets/sounds/pokemon_wall_bump.mp3"
    if event not in valid_params:
        raise ValueError("Event string not valid")

    sound = pygame.mixer.Sound(sound_file)
    sound_thread = threading.Thread(target=sound.play, daemon=True)
    sound_thread.start()
